from flask import Flask, render_template, redirect, request
from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)

psuedoDB = []

@app.route('/')
def home():
    return render_template('home.html', DB=psuedoDB)

@app.route('/handle')
def submit():
    todo = request.args["action"]
    time = request.args["time"]
    priority = request.args["priority"]
    event = (todo, time, priority)
    psuedoDB.append(event)
    return redirect('/')