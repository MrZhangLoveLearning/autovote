# coding=utf-8
from requests.exceptions import RequestException 
import logging
from requests import Session
import json
def vote_login(username,passwd):
	"""login in the univs
	Args:
		username: the account name
		passwd: the passwd

	Returns:
		the session

	"""
	try:
		s=Session()
		sso_url='http://uzone.univs.cn/sso.action'
		sso_data={}
		sso_data['gUser.loginName']=username
		sso_data['gUser.password']=passwd
		r=s.post(sso_url,data=sso_data)
		if not r.content.find('<code>0</code>') > 0 :
			return None
		res1=s.get('http://mzml.univs.cn:8081/common/checkcode')
		code=json.loads(res1.content)
		check_sso_url=('http://uzone.univs.cn/checkSSOLogin.action?token=%s&subSiteId=%s&checkCode=%s&returnUrl=http://mzml.univs.cn:8081/land.html')
		res2=s.get(check_sso_url%(code['data']['date'],code['data']['subSiteId'],code['data']['checkout'],))
		codes=res2.url
		sign_in='http://mzml.univs.cn:8081/user/sigin'
		sign_data={}
		sign_data['uid']=codes.split('?')[1].split('&')[1].split('=')[1]
		sign_data['token']=code['data']['date']
		sign_data['checkcode']=codes.split('?')[1].split('&')[0].split('=')[1]
		s.post(sign_in,data=sign_data)
		return s
	except RequestException:
		logging.exception("Login RequestException :"+username)
		return None

def auto_vote(session,account):
	
	vote=[]
	data1={}
	data1['type']='1'
	data1['id']='246'
	vote.append(data1)
	data2={}
	data2['type']='2'
	data2['id']='188'
	vote.append(data2)
	data3={}
	data3['type']='2'
	data3['id']='187'
	vote.append(data3)	
	for data in vote:
		try:
			r=session.post('http://mzml.univs.cn:8081/user/addvote',data=data)
			logging.info(r.content)
			code=json.loads(r.content)
			if not code['status'] :
				logging.warning('fail'+account.account+' : '+account.passwd)
		except RequestException:
			logging.exception("Vote RequestException :"+account.account)



    

        """


	>>> s=vote_login('loveyiyi02@163.com','yixin123')
	>>> print s.get('http://mzml.univs.cn:8081/common/issigin').content
	{"status":true,"message":"成功","data":{"isSigin":true}}
	>>> auto_vote(s)
	{"status":true,"message":"成功","data":null}



        """



s=vote_login('hsh081@126.com','888888'.strip())
print s.get('http://mzml.univs.cn:8081/common/issigin').content
print s.cookies.keys()