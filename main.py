from flask import Flask, render_template, redirect, request, flash, session, url_for
from werkzeug.utils import secure_filename  # upload images
import os
from flask_socketio import (
    SocketIO,
    emit,
    send,
    join_room,
    leave_room,
)  # replaces post requests
import smtplib


app = Flask(__name__)
app.config["SECRET_KEY"] = "hello"  # use session to save personal data to so user doesnt have to log in over and over
socketio = SocketIO(app)  # init the socket connection


@app.route("/")
def index():
    return render_template("index.html")


@socketio.on("contact")
def contact(msg):
    print(msg)
    
    email_address = 'dartagnansams1@yahoo.com'
    Subject = 'Subject: From portfolio website\n\n'
    content = f'From:{msg["name"]}\n By:{msg["email"]}\n\n{msg["message"]}' 
    footer = '- Portfolio Website' 
    passcode = os.environ.get("yahoo_api_key")
    conn = smtplib.SMTP_SSL('smtp.mail.yahoo.com', 465) 
    conn.ehlo()
    conn.login(email_address, passcode)
    conn.sendmail(email_address,email_address,Subject + content + footer)
    conn.quit()


if __name__ == "__main__":
    socketio.run(app,debug=True)
