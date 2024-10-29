from flask import Flask, request

app = Flask(__name__)


@app.route('/')
def hello():
    return 'Hello, World!'

import db

@app.route("/photos.json")
def index():
    return db.photos_all()