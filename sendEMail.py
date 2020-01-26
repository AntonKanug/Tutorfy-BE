# spjlkcarlexiftlf


import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email import encoders 

def sendEMail(email, title):
     ##Initializing  Server
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    ##Login to server
    #server.login('antondilon2@gmail.com', 'drpehshhdqzshmju')
    server.login('noreplytutorfy@gmail.com', 'spjlkcarlexiftlf')

    ##Creating Message
    msg = MIMEMultipart() 
    msg['From'] = 'Tutorfy'
    msg['Subject'] = 'New request for a student for' + title


    html = """\
                <!DOCTYPE html><h3>New Request Email!</h3>"""

    text = MIMEText(html, 'html')
    msg.attach(text)


    server.sendmail(
                    'noreplyPriceWatch@gmail.com',
                    email,
                    msg.as_string()
                )
    print("📤  Email Sent to: %s" % email)
    server.quit
