from flask import Flask, request

app = Flask(__name__)


@app.route('/welcome')
def welcome():
    """says welcome"""
    return "welcome"


@app.route('/welcome/home')
def welcome_home():
    """says welcome home"""
    return "welcome home"


@app.route('/welcome/back')
def welcome_back():
    """says welcome back"""
    return "welcome back"
