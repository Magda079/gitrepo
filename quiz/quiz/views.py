#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  views.py

from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route("/")
def hello():
    # return "Hello World!"
    return render_template('index.html')

@app.route("/lista")
def lista():
    pytania = Pytanie().select()
    if not pytania.count(): 
        pass
    return render_template('lista.html', pytania=pytania)

@app.route("/klasa")
def klasa():
    return "<h1>Klasa 3A wita!</h1>"

