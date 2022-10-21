# FLASK_APP=app.py FLASK_ENV=development flask run
from turtle import heading
from pure_eval import group_expressions

from flask import Flask
from flask import Flask, flash, redirect, render_template, request, session, jsonify
import json

app = Flask(__name__)  

# @app.route("/")
# def home():
#   return render_template("h.html")  


@app.route("/")
def experiment(): 
  return render_template("index2.html")     


if __name__=='__main__':
  app.run(debug=True,port=5000) 