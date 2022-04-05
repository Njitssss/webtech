from flask import Flask, render_template, url_for, redirect, request 
from flask_sqlalchemy import SQLAlchemy
import os
import sqlite3

currentLocation = os.path.dirname(os.path.abspath(__file__))

app = Flask(__name__)


#################################################################

@app.route("/")
def index():
    return render_template("z&d_homepage.html")

#################################################################

@app.route("/login", methods=["POST", "GET"])
def login():
    return render_template("z&d_login.html")
    
#################################################################

@app.route("/register", methods=["GET", "POST"])
def register():
    return render_template("z&d_register.html")

#################################################################

if __name__ == "__main__":
    app.run(debug=True)

