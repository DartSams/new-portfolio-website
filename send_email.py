# import smtplib

# def main(sender,sender_email,message):
#     login = "dartagnansamsd@gmail.com"
#     rec = "godofanime72@gmail.com"
#     password = "Dartagnan19@"
#     # message = "hello world"
#     # creates SMTP session
#     s = smtplib.SMTP_SSL('smtp.googlemail.com', 465)
#     s.ehlo()
#     s.starttls()
#     # s.ehlo()
    
#     # Authentication
#     # try:
#     s.login(login, password)
#     # except:
#     #     print("Login Credentials is wrong.")

#     # message to be sent
#     message = f"""
#         From : {sender}-{sender_email}
#         body: {message}
#     """
    
#     # sending the mail
#     try:
#         s.sendmail(sender, rec, message)
#     except:
#         print("Email failed to send")
    
#     # terminating the session
#     s.quit()



# if __name__ == "__main__":
#     main()




# # import smtplib

# sender = "dartagnansamsd@gmail.com"
# rec = "godofanime72@gmail.com"
# password = "Dartagnan19@"
# message = "hello world"

# # server = smtplib.SMTP("smtp.gmail.com",587)
# # server.starttls()
# # server.login(sender,password)
# # server.sendmail(sender,rec,message)


# from flask_mail import Mail, Message
# # from main import app

# app.config['MAIL_SERVER']='smtp.gmail.com'
# app.config['MAIL_PORT'] = 465
# app.config['MAIL_USERNAME'] = 'yourId@gmail.com'
# app.config['MAIL_PASSWORD'] = '*****'
# app.config['MAIL_USE_TLS'] = False
# app.config['MAIL_USE_SSL'] = True

# mail = Mail(app)

# def sendEmail(body,sender,recipient):
#     msg = Message(body, sender = sender, recipient = recipient)
#     msg.body = "This is the email body"
#     mail.send(msg)
#     print("email sent")

import os
# from urllib2 import Request, urlopen
from urllib.request import urlopen
from urllib.request import Request

request = Request('https://realemail.expeditedaddons.com/?api_key=N2568D4YH2A4L1BQS39U0CV7T87G3906JEMRZIO15FXWKP&email=email@example.org&fix_typos=false')

response_body = urlopen(request).read()

# The response is a JSON dictionary
print(response_body)