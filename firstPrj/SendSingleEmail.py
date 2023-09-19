import os

import yagmail

sender = 'app7flask@gmail.com'
receiver = '2jjnkjca@10mail.tk'

subject = "This is a test mail"

contents = """
here is the content of the mail"""

yMail = yagmail.SMTP(user=sender, password=os.getenv('PASSWORD'))

yMail.send(to=receiver, subject=subject, contents=contents)

print("Email Send")
