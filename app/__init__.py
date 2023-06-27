import os
from flask import Flask, render_template, request
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)

#/work / experience / education / places we visited
# updated flask routes

@app.route('/')
def index():
    return render_template('index.html', title="MLH Fellow", url=os.getenv("URL"))

@app.route('/Work')  # Define the route for /Work
def Work():
    return render_template('Work.html', title="Work", url=os.getenv("URL"))

# Hobbies data
hobbyData = [
    {"imgSource": "/static/img/logo.jpg",
    "name": "True Crime Podcasts", 
    "description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit."},
    {"imgSource": "/static/img/logo.jpg", 
    "name": "Soccer", 
    "description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit."},
    {"imgSource": "/static/img/logo.jpg", 
    "name": "Traveling", 
    "description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit."},
    {"imgSource": "/static/img/logo.jpg", 
    "name": "Gardening", 
    "description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit."}
]

@app.route('/Hobbies')  # Define the route for /Hobbies
def Hobbies():
    context ={
        "hobbyData": hobbyData
    }
    return render_template('hobbies.html', title="Hobbies", url=os.getenv("URL"), **context)

@app.route('/Locations')  # Define the route for /Map
def Map():
    return render_template('Locations.html', title="Location", url=os.getenv("URL"))