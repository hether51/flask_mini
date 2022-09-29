from colorama import Cursor
from flask import Flask
from datetime import datetime
import json,time
import mysql.connector


app = Flask(__name__)

@app.route("/")
def hello_world():
    t = datetime.now().isoformat(timespec='minutes')
    return "<h1>Hello docker! @2022/5/31(23:56)</h1>"

@app.route("/widgets")
def get_widgets():
    mydb = mysql.connector.connect(
        host="mysqldb",
        user="root",
        password="xiaoniu@jam",
        database="jam_flask_db"
    )

    cursor = mydb.cursor()

    cursor.execute("select * from widgets")

    row_headers=[x[0] for x in cursor.description] #this will extract row headers

    results = cursor.fetchall()
    json_data=[]
    for result in results:
        json_data.append(dict(zip(row_headers,result)))

    cursor.close()


    return json.dumps(json_data)
    #return "test"

if __name__ == "__main__":
    app.run(debug=True,host="0.0.0.0")
