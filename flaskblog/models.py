from datetime import datetime,timezone,timedelta
from flaskblog import db,login_manager,app
from flask_login import UserMixin
import jwt

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model,UserMixin):
    id = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(20),unique=True,nullable=False)
    email = db.Column(db.String(120),unique=True,nullable=False)
    image_file = db.Column(db.String(20),nullable=False,default='default.jpg')
    password = db.Column(db.String(60),nullable=False)
    posts = db.relationship('Post',backref='author',lazy=True)

    def get_reset_token(self,expired_delta=timedelta(seconds=300)):
        payload = self.id
        secrets = app.config['SECRET_KEY']
        token = jwt.encode({"user_id":payload,\
                "exp":datetime.now(tz=timezone.utc)+expired_delta},\
                secrets,algorithm="HS256")
        return token

    @staticmethod
    def verify_reset_token(token):
        secrets = app.config['SECRET_KEY']
        try:
            payload = jwt.decode(token,secrets,algorithms=["HS256"])
        except jwt.ExpiredSignatureError:
            return None
        id = payload["user_id"]
        return User.query.get(id)

    def __repr__(self) -> str:
        return f"User('{self.username}', '{self.email}', '{self.image_file}',{self.id})"


class Post(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    title = db.Column(db.String(100),nullable=True)
    date_posted = db.Column(db.DateTime,nullable=False,default=datetime.utcnow)
    content = db.Column(db.Text,nullable=False)
    user_id = db.Column(db.Integer,db.ForeignKey('user.id'),nullable=False)
    def __repr__(self) -> str:
        return f"Post('{self.id}','{self.title}','{self.date_posted}',{self.user_id})"