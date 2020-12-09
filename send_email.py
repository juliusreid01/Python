import smtplib 

#SMTP.sendmail("no-reply@jreid.com", "pacman4e@gmail.com", "Hello World")


def send_email(toAddr, subject, body):
    msg = 'Subject {}\n\n{}'.format(subject,body)
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
        server.login("pacman4e@gmail.com", "")
        server.sendmail('python@jreid.com', toAddr, msg)

#send_email('pacman4e@gmail.com','Hello World',"The quick brown fox\nJumped over the moon")

