import os
from flask import Flask, render_template, request
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html', title="MLH Fellow", url=os.getenv("URL"))

@app.route('/Margaret')  # Define the route for /Margaret
def Margaret():
    return render_template('Margaret.html', title="Margaret Diaz", url=os.getenv("URL"))

@app.route('/Gaby')  # Define the route for /Margaret
def Gaby():
    return render_template('Gaby.html', title="Gaby Liera", url=os.getenv("URL"))