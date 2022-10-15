from colorama import Cursor
from flask import Flask,render_template,url_for
from datetime import datetime
import json,time
#import mysql.connector


app = Flask(__name__)
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
    return render_template('about.html')

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
