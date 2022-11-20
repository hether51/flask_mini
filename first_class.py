import json
from flaskblog import app,db
from flaskblog.models import Post

app.app_context().push()

f = open('posts.json')
data = json.load(f)

for p1 in data:
    post = Post(title=p1['title'],content=p1['content'],user_id=p1['user_id'])
    db.session.add(post)
db.session.commit()


t1 = Post.query.all()
print(t1)



