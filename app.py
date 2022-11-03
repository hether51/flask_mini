from datetime import datetime
from enum import unique
from colorama import Cursor
from flask import Flask,render_template,url_for,flash,redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from forms import RegistrationForm,LoginForm
import json,time
#import mysql.connector


app = Flask(__name__)
app.config['SECRET_KEY'] = '77ceed0246b6184b5fe46f96d72fa4b8'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy()
db.init_app(app)

class User(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(20),unique=True,nullable=False)
    email = db.Column(db.String(120),unique=True,nullable=False)
    image_file = db.Column(db.String(20),nullable=False,default='defualt.jpg')
    password = db.Column(db.String(60),nullable=False)
    posts = db.relationship('Post',backref='author',lazy=True)

    def __repr__(self) -> str:
        return f"User('{self.username}', '{self.email}', '{self.image_file}')"

class Post(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    title = db.Column(db.String(100),nullable=True)
    date_posted = db.Column(db.DateTime,nullable=False,default=datetime.utcnow)
    content = db.Column(db.Text,nullable=False)
    user_id = db.Column(db.Integer,db.ForeignKey('user.id'),nullable=False)
    def __repr__(self) -> str:
        return f"Post('{self.id}','{self.title}','{self.date_posted}')"



posts = [
    {
        'author': 'jam',
        'title': 'blog post1',
        'content': 'First post content',
        'date_posted': 'October 1,2022'
    },
    {
        'author': 'hether',
        'title': 'Blog post2',
        'content': 'Second post content',
        'date_posted': 'october 2,2022'
    }
]


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html',posts=posts,title='20221013')

@app.route("/about")
def about():
    return render_template('about.html',title='关于')

@app.route("/register",methods=['GET','POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'账号已经成立: {form.username.data} !','success')
        return redirect(url_for('home'))
    return render_template('register.html',title='Register',form=form)

@app.route("/login",methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@jam.com' and form.password.data == 'xiaoniu..':
            flash(f'you have logged in as {form.email.data}','success')
            return redirect(url_for('home'))
        else:
            flash('Fail to log in .Please check your username and password!','danger')
    return render_template('login.html',title='login',form=form)

# @app.route("/widgets")
# def get_widgets():
#     mydb = mysql.connector.connect(
#         host="mysqldb",
#         user="root",
#         password="xiaoniu@jam",
#         database="jam_flask_db"
#     )

#     cursor = mydb.cursor()

#     cursor.execute("select * from widgets")

#     row_headers=[x[0] for x in cursor.description] #this will extract row headers

#     results = cursor.fetchall()
#     json_data=[]
#     for result in results:
#         json_data.append(dict(zip(row_headers,result)))

#     cursor.close()


#     return json.dumps(json_data)
#     #return "test"

if __name__ == "__main__":
    app.run(debug=True,host="0.0.0.0")
