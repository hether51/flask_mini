from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField,BooleanField,EmailField
from wtforms.validators import DataRequired,Length,Email,EqualTo

class RegistrationForm(FlaskForm):
    username = StringField('用户名',validators=[DataRequired(),Length(min=2,max=20)])
    email = EmailField('邮箱',validators=[Email(),DataRequired()])
    password = PasswordField('密码',validators=[DataRequired()])
    confirm_password = PasswordField('确认密码',validators=[DataRequired(),EqualTo('password')])
    submit = SubmitField('注册')

class LoginForm(FlaskForm):
    email = StringField('邮箱',validators=[DataRequired(),Email()])
    password = PasswordField('密码',validators=[DataRequired(),Length(min=5,max=20)])
    remember = BooleanField('下次免登录？')
    submit = SubmitField('插入')
  