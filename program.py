import imaplib
import smtplib
import email
mail=imaplib.IMAP4_SSL("imap.gmail.com") #Service Provider IMAP
mail.login("ixxxxxxech@gmail.com","password") #Email and Password
mail.select('inbox')
result, data = mail.search(None, "ALL")
ids = data[0]
id_list = ids.split()
latest_email_id = id_list[-1]
result, data = mail.fetch(latest_email_id, "(RFC822)")
raw_email = data[0][1]
email_message = email.message_from_bytes(raw_email)
print(email_message['To'])
print(email.utils.parseaddr(email_message['From']))
print(email_message.items())
def get_first_text_block(self, email_message_instance):
    maintype = email_message_instance.get_content_maintype()
    if maintype == 'multipart':
        for part in email_message_instance.get_payload():
            if part.get_content_maintype() == 'text':
                return part.get_payload()
    elif maintype == 'text':
        return email_message_instance.get_payload()
