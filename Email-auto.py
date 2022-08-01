# importing modules
from email.message import EmailMessage
import ssl
import smtplib as sm

# storing sender, receiver,password, subject and message body details in variables
sender = '*******@gmail.com'
receiver = '**********@gmail.com'
password = '***********'
subject = 'This is a test message'
body = '''Just for Testing Purpose'''

# creating an object to access EmailMessage module methods
content = EmailMessage()

#setting object values with specifed keys
content['From'] = sender
content['To'] = receiver
content['Subject'] = subject
content.set_content(body)

# creating an ssl connection for secure transmission
con = ssl.create_default_context()

# declaring port values , smtp mail protocols
with sm.SMTP_SSL('smtp.gmail.com', 465, context=con) as smtp:

# login to mail and sending details to receiver side
    smtp.login(sender, password)
    smtp.sendmail(sender, receiver, content.as_string())

# if all works fine it will show success message
print('success')

