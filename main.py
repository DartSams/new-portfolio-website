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

# from send_email import sendEmail


app = Flask(__name__)
app.config["SECRET_KEY"] = "hello"  # use session to save personal data to so user doesnt have to log in over and over
socketio = SocketIO(app)  # init the socket connection

from flask_mail import Mail, Message
# from main import app

app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'dartagnansamsd@gmail.com'
app.config['MAIL_PASSWORD'] = 'Dartagnan19@'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True

mail = Mail(app)

def sendEmail(subject,body,sender,recipient):
    msg = Message(subject, sender = sender, recipients = [recipient])
    msg.body = body
    mail.send(msg)
    print("email sent")


@app.route("/")
def index():

    return render_template("index.html")

import sendgrid
import os
from sendgrid.helpers.mail import *
@socketio.on("contact")
def contact(msgj):
    print(msgj)

    sg = sendgrid.SendGridAPIClient(api_key=os.environ.get("key"))
    from_email = Email("dartagnansamsd@example.com")
    to_email = To("godofanime72@example.com")
    subject = "Sending with SendGrid is Fun"
    content = Content("text/plain", "and easy to do anywhere, even with Python")
    mail = Mail(from_email, to_email, subject, content)
    print(mail)
    response = sg.client.mail.send.post(request_body=mail.get())
    print(response.status_code)
    print(response.body)
    print(response.headers)


if __name__ == "__main__":
    socketio.run(app,debug=True)
