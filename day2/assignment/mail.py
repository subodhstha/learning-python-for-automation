import smtplib
from email.message import EmailMessage

email1 = 'shresthasubodh73@gmail.com'
pasw = 'hslkhcflska'

msg = EmailMessage()
msg['Subject'] = "assignment"
msg['From'] = email1
msg['To'] = 'pdsc.nepal@gmail.com'
msg.set_content('assignment..')
with open('assignment.pdf','rb') as f:
    file_data = f.read()
    file_type = 'png'
    file_name = f.name
msg.add_attachment(file_data, maintype = 'application', subtype = 'octet-steam', filename = file_name)
with smtplib.SMTP_SSL('smtp.gmail.com',465) as smtp:
    smtp.login(email1,pasw)
    smtp.send_message(msg)
