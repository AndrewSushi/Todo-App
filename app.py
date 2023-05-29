from flask import Flask, render_template, redirect, request
from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/handle')
def submit():
    todo = request.args["action"]
    return render_template('form_submit.html', todo=todo)