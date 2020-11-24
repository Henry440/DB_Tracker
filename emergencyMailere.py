import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

from files.configs import LOG_FILE, OUTPUT

def mail2():
    sender_email = "oliver.audehm@gmail.com"
    receiver_email = "oliver.audehm@gmail.com"
    password = "KENNWORT"

    message = MIMEMultipart("alternative")
    message["Subject"] = "Kritisch DB_Tracker"
    message["From"] = sender_email
    message["To"] = receiver_email

    # Create the plain-text and HTML version of your message
    text = """\
    Das system ist Wahrscheinlich abgestürtzt!"""
    html = """\
    <h1 style="color:red;"><strong>Achtung!!!</strong></h1>
<p>Du solltest Zeitnah es &uuml;berpr&uuml;fen!!!</p>
<p>
  Es könnte sonst zu einem Datenverlust kommen. 
</p>
<p>Der Befehl für den SSH zugang von extern ist :<br> ssh nnnnn@nnnnn.de/p>
<br>
<p>
  Solltest du nicht der genannte Empfänger oli*****.a******@gmail.com sein, bitte ich dich diese E-Mail umgehend zu löschen!
</p>

<p>
  Diese E-Mail wurde automatisch Versand
</p>
    """

    # Turn these into plain/html MIMEText objects
    part1 = MIMEText(text, "plain")
    part2 = MIMEText(html, "html")

    part3 = MIMEBase('application', "octet-stream")
    part3.set_payload(open(LOG_FILE, "rb").read())
    encoders.encode_base64(part3)
        
    part3.add_header('Content-Disposition', 'attachment; filename="logFile.txt"')

    part4 = MIMEBase('application', "octet-stream")
    part4.set_payload(open(OUTPUT, "rb").read())
    encoders.encode_base64(part4)
        
    part4.add_header('Content-Disposition', 'attachment; filename="aktuelleDaten.csv"')


    # Add HTML/plain-text parts to MIMEMultipart message
    # The email client will try to render the last part first
    message.attach(part1)
    message.attach(part2)
    message.attach(part3)
    message.attach(part4)

    # Create secure connection with server and send email
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(
            sender_email, receiver_email, message.as_string()
        )
