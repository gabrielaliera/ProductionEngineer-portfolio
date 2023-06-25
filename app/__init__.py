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

@app.route('/Hobbies')  # Define the route for /Hobbies
def Hobbies():
    return render_template('Hobbies.html', title="Hobbies", url=os.getenv("URL"))

@app.route('/Locations')  # Define the route for /Map
def Map():
    return render_template('Locations.html', title="Location", url=os.getenv("URL"))