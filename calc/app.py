from flask import Flask, request
from operations import add, sub, mult, div

app = Flask(__name__)

@app.route('/')
def home_page():
    return "Home Page"

oper={
    'add': add,
    "sub": sub,
    "mult": mult,
    "div": div,
}

@app.route('/math/<function>')
def math_page(function):
    a = int(request.args["a"])
    b = int(request.args["b"])
    ans = oper[function](a,b)
    return str(ans)