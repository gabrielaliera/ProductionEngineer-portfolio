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

workData = [
    {
        "title": "Production Engineering Intern",
        "employer": "MHL Fellowship",
        "date": "June 2023 - Present",
        "description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit."
    },
    {   
        "title": "Software Engineering Intern",
        "employer": "Meta",
        "date": "June 2022 - September 2022", 
        "description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit."
    },
    {   
        "title": "Participant",
        "employer": "MHL Hackaton",
        "date": "June 2022",
        "description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit."
    },
    {
        "title": "President",
        "employer": "The Club",
        "date": "Oct 2021 - May 2022", 
        "description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit."
    }
]

@app.route('/Work')  # Define the route for /Work
def Work():
    context ={
        "workData": workData
    }
    return render_template('Work.html', title="Work", url=os.getenv("URL"), **context)

# Hobbies data
hobbyData = [
    {"imgSource": "/static/img/podcast.jpg",
    "name": "True Crime Podcasts", 
    "description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit."},
    {"imgSource": "/static/img/soccer.jpg", 
    "name": "Soccer", 
    "description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit."},
    {"imgSource": "/static/img/travel.jpg", 
    "name": "Traveling", 
    "description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit."},
    {"imgSource": "/static/img/garden.jpg", 
    "name": "Gardening", 
    "description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit."}
]

@app.route('/Hobbies')  # Define the route for /Hobbies
def Hobbies():
    context = {
        "hobbyData": hobbyData
    }
    return render_template('Hobbies.html', title="Hobbies", url=os.getenv("URL"), **context)

@app.route('/Locations')  # Define the route for /Map
def Map():
    return render_template('Locations.html', title="Location", url=os.getenv("URL"))