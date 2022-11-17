# using SendGrid's Python Library
# https://github.com/sendgrid/sendgrid-python
import sendgrid
import os
from sendgrid.helpers.mail import Mail,Email,To,Content

sg = sendgrid.SendGridAPIClient(api_key= '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' )
from_email = Email("cinthamani2002@gmail.com") #Change to your verified sender
to_email = To("cinthu143@gmail..edu.in.com") #Change to your recipient
subject = "Sending with SendGrid is Fun"
content = Content("text/plain", "and easy to do anywhere, even with Python")
mail = Mail(from_email, to_email, subject, content)


#Get a JSON-ready representation of the Mail object
mail_json = mail.get()

#Send an HTTP POST request to /mail/send
response = sg.client.mail.send.post(request_body=mail.get())
print(response.status_code)
print(response.body)
print(response.headers)

