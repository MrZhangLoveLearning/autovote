# coding=utf-8
import logging
import os
import connection
from model import Account
import vote

work_level=logging.WARNING
debug_level=logging.DEBUG
# set up logging to file - see previous section for more details
logging.basicConfig(level=work_level,
                    format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
                    datefmt='%m-%d %H:%M',
                    filename=connection.base_dir+'log.txt',
                    filemode='a+')
# define a Handler which writes INFO messages or higher to the sys.stderr
console = logging.StreamHandler()
console.setLevel(logging.INFO)
# set a format which is simpler for console use
formatter = logging.Formatter('%(name)-12s: %(levelname)-8s %(message)s')
# tell the handler to use this format
console.setFormatter(formatter)
# add the handler to the root logger
logging.getLogger('').addHandler(console)
 
# Now, we can log to the root logger, or any other logger. First the root...

 
def is_full_name(name):
	ord_num=name.find('@')
	if ord_num > 0:
		return 1
	else:
		return 0
session=connection.init_db()
query=session.query(Account)
for account in query.all():
	web_se=vote.vote_login(account.account,account.passwd)
	if web_se:
		vote.auto_vote(web_se,account)
	elif is_full_name(account.account.strip()):
		session.delete(account,web_se)
		session.commit()
		logging.warning('delete '+ac.account)
	elif vote.vote_login(account.account.strip()+'@qq.com',account.passwd.strip()):
		vote.auto_vote(vote.vote_login(account.account.strip()+'@qq.com',account.passwd.strip()),account)
		ac=Account(account=account.account.strip()+'@qq.com',passwd=account.passwd.strip())
		session.add(ac)
		session.delete(account)
		session.commit()
		logging.warning('add '+ac.account)
	elif vote.vote_login(account.account.strip()+'@163.com',account.passwd.strip()):
		vote.auto_vote(vote.vote_login(account.account.strip()+'@163.com',account.passwd.strip()),account)
		ac=Account(account=account.account.strip()+'@163.com',passwd=account.passwd.strip())
		session.add(ac)
		session.delete(account)
		session.commit()
		logging.warning('add '+ac.account)
	else:
		session.delete(account)
		session.commit()
		logging.warning('delete '+ac.account)		












