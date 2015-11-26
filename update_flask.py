# coding=utf-8
from flask import Flask
from flask import request
app = Flask(__name__)
# app.debug=True
@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/update', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['file']
        f.save('G:\\Python\\Project\\autovote\\file')
        return 'OK'
    else:
    	return '''
		<!DOCTYPE html>
		<html>
		<head>
		<meta charset="utf-8" />
		<meta name="viewport" content="width=device-width" />
		<link rel="icon" href="http://cdn-img.easyicon.net/png/16/1614.png">
		<link rel="stylesheet" href="http://cdn.bootcss.com/bootstrap/3.3.4/css/bootstrap.min.css">
		<link rel="stylesheet" href="../../static/css/signin.css" />
		<script src="http://cdn.bootcss.com/jquery/1.11.2/jquery.min.js"></script>
		<script src="http://cdn.bootcss.com/bootstrap/3.3.4/js/bootstrap.min.js"></script>
		</head>
		<body>
		<div class="container">
		<form action="/update" class="form-signin FontComic" method="post" enctype="multipart/form-data">
		<h2 class="form-signin-heading">文件上传</h2>
		<input class="form-control text-box single-line password" id="Password" name="file" placeholder="文件" type="file" value="" />
		<button class="btn btn-lg btn-primary btn-block" type="submit">上传</button>
		</form> 
		</div>
		</body>
		</html>
    	'''
if __name__ == '__main__':
    app.run(host='0.0.0.0')
