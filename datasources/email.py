import imaplib
import email
from email.header import decode_header

# account credentials
username = "youremailaddress@provider.com"
password = "yourpassword"


# create an IMAP4 class with SSL 
imap = imaplib.IMAP4_SSL("imap.gmail.com")
# authenticate
imap.login(username, password)


# select the mailbox I want to delete in
# if you want SPAM, use imap.select("SPAM") instead
imap.select("INBOX")

# search for specific mails by sender
status, messages = imap.search(None, 'FROM "googlealerts-noreply@google.com"')

# to get mails by subject
status, messages = imap.search(None, 'SUBJECT "Thanks for Subscribing to our Newsletter !"')


# to get mails after a specific date
status, messages = imap.search(None, 'SINCE "01-JAN-2020"')
# to get mails before a specific date
status, messages = imap.search(None, 'BEFORE "01-JAN-2020"')



# to get all mails
status, messages = imap.search(None, "ALL")

# convert messages to a list of email IDs
messages = messages[0].split(b' ')

