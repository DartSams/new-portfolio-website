from flask import Flask, render_template, redirect, request, flash, session, url_for
from werkzeug.utils import secure_filename  # upload images
import os
import time  # return current date & time
from flask_socketio import (
    SocketIO,
    emit,
    send,
    join_room,
    leave_room,
)  # replaces post requests


app = Flask(__name__)
app.config["SECRET_KEY"] = "hello"  # use session to save personal data to so user doesnt have to log in over and over
socketio = SocketIO(app)  # init the socket connection


@app.route("/")
def index():
    return render_template("index.html")


@socketio.on("contact")
def contact(msg):
    print(msg)

if __name__ == "__main__":
    socketio.run(app,debug=True)
