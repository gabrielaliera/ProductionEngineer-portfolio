import os
from flask import Flask, render_template, request
from dotenv import load_dotenv
from peewee import *
import datetime 
from playhouse.shortcuts import model_to_dict 
from app.data import workData, eduData, hobbyData

load_dotenv()
app = Flask(__name__)


if os.getenv("TESTING"):
    print("Running in test mode")
    mydb = SqliteDatabase("file:memory?mode=memory&cache=shared", uri=True)
else:
    mydb = MySQLDatabase(os.getenv("MYSQL_DATABASE"),
                user=os.getenv("MYSQL_USER"),
                password=os.getenv("MYSQL_PASSWORD"),
                host=os.getenv("MYSQL_HOST"),
                port=3306
    )
print(mydb)

class TimelinePost(Model):
    name = CharField()
    email = CharField()
    content = TextField()
    created_at = DateTimeField(default=datetime.datetime.now)

    class Meta:
        database = mydb

mydb.connect()
mydb.create_tables([TimelinePost])

#------------------------------------------------------------------
@app.route('/')
def index():
    return render_template('index.html', title="Gabriela Liera", url=os.getenv("URL"))

@app.route('/aboutme')
def aboutMe():
    context ={
        "workData": workData,
        "eduData": eduData
    }
    return render_template('aboutme.html', title="Gabriela Liera", url=os.getenv("URL"), **context)

#--------------------------------------------------------------
@app.route('/api/timeline_post', methods=['POST'])
def post_time_line_post():
    if not request.form.get('name') or request.form['name'] == "":
        return "Invalid name", 400
    if not request.form.get('email') or request.form['email'] == "":
        return "Invalid email", 400
    if not request.form.get('content') or request.form['content'] == "":
        return "Invalid content", 400
    name = request.form['name']
    email = request.form['email']
    content = request.form['content']
    valid_email = "@" in email and "." in email
    if valid_email == False:
        return "Invalid email", 400
    timeline_post =TimelinePost.create(name=name, email=email, content=content)
    return model_to_dict(timeline_post)

@app.route('/api/timeline_post', methods=['GET'])
def get_time_line_post():
    return {
        'timeline_posts' : [
            model_to_dict(p)
            for p in TimelinePost.select().order_by(TimelinePost.created_at.desc())
        ]
    }

@app.route('/api/timeline_post', methods=["DELETE"])
def delete_time_line_post():
    post_id = request.form["id"] #ID sent in request header
    #post_id = request.args.get('post_id') #Assumes the post_id is given in url query parameters - add postID to arg of function
    try:
        post = TimelinePost.get_by_id(post_id)
        post.delete_instance()
        return model_to_dict(post) #Return deleted post in dic format
    except TimelinePost.DoesNotExist:
        return {"error": "Timeline post not found"}, 404
    
@app.route('/timeline')
def timeline():
    return render_template('timeline.html', title="Timeline", url=os.getenv("URL"))
