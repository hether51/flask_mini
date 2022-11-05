from flask import render_template,url_for,flash,redirect
from flaskblog import app
from flaskblog.forms import RegistrationForm, LoginForm
from flaskblog.models import User,Post





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