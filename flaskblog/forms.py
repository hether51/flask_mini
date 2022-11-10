from flask_wtf import FlaskForm
from flask_wtf.file import FileField,FileAllowed,FileRequired
from flask_login import current_user
from wtforms import StringField,PasswordField,SubmitField,BooleanField,EmailField
from wtforms.validators import DataRequired,Length,Email,EqualTo,ValidationError
from flaskblog.models import User

class RegistrationForm(FlaskForm):
    username = StringField('用户名',validators=[DataRequired(),Length(min=2,max=20)])
    email = EmailField('邮箱',validators=[Email(),DataRequired()])
    password = PasswordField('密码',validators=[DataRequired()])
    confirm_password = PasswordField('确认密码',validators=[DataRequired(),EqualTo('password')])
    submit = SubmitField('注册')

    def validate_username(self,username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('Username is taken.Please choose another one!')

    def validate_email(self,email):
        mail = User.query.filter_by(email=email.data).first()
        if mail:
            raise ValidationError('email is taken.Please choose another one!')

class LoginForm(FlaskForm):
    email = StringField('邮箱',validators=[DataRequired(),Email()])
    password = PasswordField('密码',validators=[DataRequired(),Length(min=2,max=20)])
    remember = BooleanField('下次免登录？')
    submit = SubmitField('插入')

class UpdateAccountForm(FlaskForm):
    username = StringField('用户名',validators=[DataRequired(),Length(min=2,max=20)])
    email = StringField('邮箱',validators=[Email(),DataRequired()])
    picture = FileField('用户自选图片',validators=[FileAllowed(['jpg','png','webp'],'只接受图片')])
    submit = SubmitField('更新')
    def validate_username(self,username):
        if username.raw_data is not None and username.data != current_user.username:
            user = User.query.filter_by(username=username.data).first()
            if user:
                raise ValidationError('Username is taken.Please choose another one!')

    def validate_email(self,email):
        if email.raw_data is not None and email.data != current_user.email:
            mail = User.query.filter_by(email=email.data).first()
            if mail:
                raise ValidationError('email is taken.Please choose another one!')
