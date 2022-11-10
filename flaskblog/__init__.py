from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import json,time
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
#import mysql.connector

# after import app in console , add the context: app.app_context().push()
# or just flask shell
app = Flask(__name__)
app.config['SECRET_KEY'] = '77ceed0246b6184b5fe46f96d72fa4b8'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy()
db.init_app(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = "login"
login_manager.login_message = u"您没有登录，请输入账号密码："
login_manager.login_message_category = "info"

from flaskblog import routes

'''
1.+ URL 中+号表示空格 %2B
2.空格 URL中的空格可以用+号或者编码 %20
3./ 分隔目录和子目录 %2F
4.? 分隔实际的 URL 和参数 %3F
5.% 指定特殊字符 %25
6.# 表示书签 %23
7.& URL 中指定的参数间的分隔符 %26
8.= URL 中指定参数的值 %3D
'''