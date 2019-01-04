#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  views.py

from flask import Flask
from flask import render_template, request 

from modele import Kategoria, Pytanie, Odpowiedz

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
    

@app.route("/quiz", methods= ['GET', 'POST'])
def quiz():
    
    print(request.form)
    
    if request.method == 'POST':
        wynik = 0 
        for pid, oid in request.form.items():
            if Odpowiedz().get(Odpowiedz.id == int(oid)).odpok:
                wynik += 1
    pass
    
    pytania = Pytanie().select().join(Odpowiedz).distinct()
    return render_template('quiz.html', pytania=pytania)
    
