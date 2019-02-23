def send_email(user, pwd, recipient, subject, body):

    """ This functions allows sending emails via gmail.
Just make sure unsafe Apps in your Google Account are allowed.
user and pwd are your google login details.
You can pass a single address or a list of addresses as recipient """
    
    import smtplib

    FROM = user
    # Checks if recipient is from type list otherwise it makes an anonymous list.
    TO = recipient if isinstance(recipient, list) else [recipient]
    SUBJECT = subject
    TEXT = body

    # Prepare actual message. It means formatting.
    message = """From: %s\nTo: %s\nSubject: %s\n\n%s""" % (FROM, ",".join(TO), SUBJECT, TEXT)

    # Try to connect and send the email.
    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.ehlo()
        server.starttls()
        server.login(user, pwd)
        server.sendmail(FROM, TO, message)
        server.close()
        print("successfully sent the mail")
    except:
        print("failed to send mail")

