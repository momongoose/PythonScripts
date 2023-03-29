import smtplib
# set up the SMTP server
s = smtplib.SMTP(host='smtp-mail.outlook.com', port=587)
pas = "pas"
s.starttls()
s.login("login@mail.com", pas)
sender_email = "sender@mail.com"
receiver_email = "receiver@mail.com"
message = """\
Subject: Hi there

This message is sent from Python."""
s.sendmail(sender_email, receiver_email, message)
