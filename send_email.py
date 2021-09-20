import smtplib

def main(sender,sender_email,message):
    login = "dartagnansamsd@gmail.com"
    rec = "godofanime72@gmail.com"
    password = "Dartagnan19@"
    # message = "hello world"
    # creates SMTP session
    s = smtplib.SMTP("smtp.gmail.com", 587)
    s.ehlo()
    s.starttls()
    # s.ehlo()
    
    # Authentication
    try:
        s.login(login, password)
    except:
        print("Login Credentials is wrong.")

    # message to be sent
    message = f"""
        From : {sender}-{sender_email}
        body: {message}
    """
    
    # sending the mail
    try:
        s.sendmail(sender, rec, message)
    except:
        print("Email failed to send")
    
    # terminating the session
    s.quit()



if __name__ == "__main__":
    main()




# import smtplib

sender = "dartagnansamsd@gmail.com"
rec = "godofanime72@gmail.com"
password = "Dartagnan19@"
message = "hello world"

# server = smtplib.SMTP("smtp.gmail.com",587)
# server.starttls()
# server.login(sender,password)
# server.sendmail(sender,rec,message)