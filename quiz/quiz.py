#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  quiz.py
#  

from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

def main(args):
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
