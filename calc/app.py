# Put your app in here.
from flask import Flask, request
from operations import add, sub, mult, div

app = Flask(__name__)


@app.route('/add')
def add():
    """returns sum of a, b"""
    a = int(request.args["a"])
    b = int(request.args["b"])
    return f"{a+b}"


@app.route('/sub')
def sub():
    """returns difference of a, b"""
    a = int(request.args["a"])
    b = int(request.args["b"])
    return f"{a-b}"


@app.route('/mult')
def mult():
    """returns product of a, b"""
    a = int(request.args["a"])
    b = int(request.args["b"])
    return f"{a*b}"


@app.route('/div')
def div():
    """returns quotient of a, b"""
    a = int(request.args["a"])
    b = int(request.args["b"])
    return f"{a/b}"
