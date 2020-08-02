import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
host_address = "sarawinget0@gmail.com"
host_pass = "Krishna321"
guest_address = "sarawinget0@gmail.com"
subject = "Regarding pod status "
content = '''Hello, Developer this is an email regarding your last job. The pod testing failed kindly review.
			THANK YOU ...'''
message = MIMEMultipart()
message['From'] = host_address
message['To'] = guest_address
message['Subject'] = subject
message.attach(MIMEText(content, 'plain'))
session = smtplib.SMTP('smtp.gmail.com', 587)
session.starttls()
session.login(host_address, host_pass)
text = message.as_string()
session.sendmail(host_address, guest_address  , text)
session.quit()
print('Successfully sent your mail')
