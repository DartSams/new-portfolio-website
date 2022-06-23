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
import smtplib,ssl


app = Flask(__name__)
app.config["SECRET_KEY"] = "hello" 
socketio = SocketIO(app)  # init the socket connection


@app.route("/")
def index():
    return render_template("index2.html")


@socketio.on("send_email")
def send_email(msg):
    print(msg)
    
    email_address = 'dartagnansams1@icloud.com'
    Subject = 'Subject: From portfolio website\n\n'
    content = f'From:{msg["name"]}\n By:{msg["email"]}\n\n{msg["message"]}' 
    footer = '- Portfolio Website' 
    passcode = os.environ.get('yahoo_api_key')
    conn = smtplib.SMTP('smtp.mail.yahoo.com', 465) 
    conn.ehlo()
    # conn.start()
    conn.starttls()
    conn.login(email_address, passcode)
    print("made it here")
    try:
        conn.sendmail(email_address,email_address,Subject + content + footer)
    except:
        print("no mail sent")
    conn.quit()

    # context = ssl.create_default_context()
    # with smtplib.SMTP('smtp.mail.yahoo.com', 587) as server:
    #     server.ehlo()  # Can be omitted
    #     server.starttls(context=context)
    #     server.ehlo()  # Can be omitted
    #     server.login('dartagnansams1@yahoo.com', passcode)
    #     server.sendmail(msg["email"], 'dartagnansams1@yahoo.com', content)

    # server = smtplib.SMTP('smtp.mail.yahoo.com', 465)
    # server.starttls()
    # server.login(email_address,"STAYOUT3434@")
    # server.sendmail("dartagnansams1@yahoo.com",msg["email"],"message sent from python")
    # print("mail sent")

if __name__ == "__main__":
    socketio.run(app,debug=True,port=8000)
