#python=3.6
# -*- coding: utf-8 -*-
"""
Synopsis: 

Created: Created on Sun Feb 14 18:59:11 2021

Sources:

Author:   John Telfeyan
          john <dot> telfeyan <at> gmail <dot> com

Distribution: MIT Opens Source Copyright; Full permisions here:
    https://gist.github.com/john-telfeyan/2565b2904355410c1e75f27524aeea5f#file-license-md
         
"""

from flask import Flask
app = Flask(__name__)

@app.route("/")
def index():
    return "<h1>Hello Azure!</h1>"

"""
if __name__=="__main__":
"""
