from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def home_page():
    return "Home Page"

@app.route('/welcome')
def welcome_page():
    return "welcome"

@app.route('/welcome/<word>')
def back_welcome_page(word):
    return f"welcome {word}"



