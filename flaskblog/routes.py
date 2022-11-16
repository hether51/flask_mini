import os,secrets
from PIL import Image
from flask import render_template,url_for,flash,redirect,request,abort
from flaskblog import app,db,bcrypt
from flaskblog.forms import RegistrationForm, LoginForm, UpdateAccountForm,PostForm
from flaskblog.models import User,Post
from flask_login import login_user,current_user,logout_user,login_required,login_manager



@app.route("/")
@app.route("/home")
def home():
    posts = Post.query.all()
    return render_template('home.html',posts=posts,title='20221013')

@app.route("/about")
def about():
    return render_template('about.html',title='关于')

@app.route("/register",methods=['GET','POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data,email=form.email.data,password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash(f'账号已经成立: {form.username.data} !','success')
        return redirect(url_for('login'))
    return render_template('register.html',title='Register',form=form)

@app.route("/login",methods=['GET','POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        #hashed_password = user.password
        if user and bcrypt.check_password_hash(user.password,form.password.data):
            login_user(user,remember=form.remember.data)
            #flash(f'you have logged in as {user.email}','success')
            next_page = request.args.get('next')
            return redirect(next_page or url_for('home')) 
        else:
            flash('Fail to log in .Please check your username and password!','danger')
    return render_template('login.html',title='login',form=form)

@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('login'))

def save_picture(form_pic):
    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(form_pic.filename)
    pic_fn = random_hex + f_ext
    pic_path = os.path.join(app.root_path,'static/profile_pics',pic_fn)
    
    output_size = (125,125)
    i = Image.open(form_pic)
    i.thumbnail(output_size)
    i.save(pic_path)
    return pic_fn


@app.route("/account",methods=['GET','POST'])
@login_required
def account():    
    form = UpdateAccountForm()
    if form.validate_on_submit():
        if form.picture.data:
            current_user.image_file = save_picture(form.picture.data)
        if current_user.username != form.username.data and current_user.email != form.email.data:
            current_user.username = form.username.data
            current_user.email = form.email.data
        db.session.commit()
        flash(f'账号已更新，下次记得用新账号登录','success')
        image_file = url_for('static',filename='profile_pics/'+current_user.image_file)        
        return render_template('account.html',title='账号',
                               image_file=image_file,form=form )
    elif request.method=='GET':
        form.username.data = current_user.username
        form.email.data = current_user.email
    image_file = url_for('static',filename='profile_pics/'+current_user.image_file)
    return render_template('account.html',title='记录',
                           image_file=image_file,form=form )
    
@app.route("/post/new",methods=['GET','POST'])
@login_required
def new_post():
    form = PostForm()
    if form.validate_on_submit():
        post = Post(title=form.title.data,content=form.content.data,user_id=current_user.id)
        db.session.add(post)
        db.session.commit()
        flash('帖子已经更新','success')
        return redirect(url_for('home'))
    return render_template('create_post.html',title='New Post',form=form,legend='新文章')

@app.route("/post/<int:post_id>")
def post(post_id):
    post = Post.query.get_or_404(post_id,"输入的flask页面错误缺失")
    return render_template('post.html',title=post.title,post=post)

@app.route("/post/<int:post_id>/update",methods=['GET','POST'])
@login_required
def update_post(post_id):
    post = Post.query.get_or_404(post_id)
    if post.author != current_user :
        abort(403)
    form = PostForm()
    if form.validate_on_submit():
        post.title = form.title.data
        post.content = form.content.data
        db.session.commit()
        flash('文章已经更新','success')
        return redirect(url_for('post',post_id=post.id))
    elif request.method == 'GET':
        form.title.data = post.title
        form.content.data = post.content
    return render_template('create_post.html',title='Update Post',
                            form=form,legend='更新post')

@app.route('/delete_post/<int:post_id>/delete',methods=['POST'])
@login_required
def delete_post(post_id):
    post = Post.query.get_or_404(post_id)
    if post.author != current_user:
        abort(403)
    
    db.session.delete(post)
    db.session.commit()
    flash('已经成功删除文章','success')
    return redirect(url_for('home'))


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