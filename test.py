# import smtplib,ssl
# from email.message import EmailMessage

# from django.dispatch import receiver

# # server = smtplib.SMTP('smtp.mail.yahoo.com', 465)
# # server.starttls()
# # server.login("dartagnansams1@icloud.com","STAYOUT3434@")
# # server.sendmail("dartagnansams1@yahoo.com","dartagnansams1@icloud.com","message sent from python")
# # print("mail sent")

# sender = "dartagnansamsd@gmail.com"
# password = "Dartagnan19@"
# email_receiver = "dartagnansams1@yahoo.com"

# subject = "from portfolio website"
# body = """
#     Testing if python can send emails
#     """

# em = EmailMessage()
# em["From"] = sender
# em["To"] = email_receiver
# em["Subject"] = subject
# em.set_content(body)

# context = ssl.create_default_context()
# with smtplib.SMTP_SSL("smtp.gmail.com",465,context=context) as smtp:
#     smtp.login("portfoliowebsite34@gmail.com","Dartagnan19@")
#     smtp.sendmail(sender,email_receiver,em.as_string())



import win32com.client as win32

olApp = win32.Dispatch("Outlook.Application")
olNS = olApp.GetNameSpace("MAPI")


mailItem = olApp.CreateItem(0)
mailItem.Subject = "hello 123"
mailItem.BodyFormat = 1
mailItem.Body = "Hello there"
mailItem.To = "dartagnansams1@icloud.com"
mailItem._oleobj_.Invoke(*(64209,0,8,0,olNS.Accounts.Item("dartagnansams1@icloud.com")))

# mailItem.Display()
# mailItem.Save()
mailItem.Send()