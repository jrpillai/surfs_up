#import flask dependency
from flask import Flask

#create new flask instance
app = Flask(__name__)

#define root
@app.route('/')
def hello_world():
    return 'Hello world'

