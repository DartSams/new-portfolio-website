from replit import web
from flask import Flask, render_template, redirect, request, flash, session, url_for
import os
import smtplib,ssl


app = Flask(__name__)
app.config["SECRET_KEY"] = "hello" 


@app.route("/")
def index():
    return render_template("index2.html")


web.run(app)
