#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  quiz.py

from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route("/")
def hello():
    # return "Hello World!"
    return render_template('index.html')

@app.route("/lista")
def lista():
    return "<h1>Witaj na serwerze</h1><h2>Aplikacja Quiz</h2>"

@app.route("/klasa")
def klasa():
    return "<h1>Klasa 3A wita!</h1>"

