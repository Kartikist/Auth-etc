import imapclient, os

# Set up your email server and login credentials
imap_server = 'imap.gmail.com'
username = 'neti.kartik@gmail.com'
password = os.getenv('PASSWORD')

# The specific email address you want to filter by
specific_email_address = 'karpekanishka@gmail.com'

# Connect to the IMAP server
imap = imapclient.IMAPClient(imap_server)

# Log in to your email account
imap.login(username, password)

# Select the mailbox (inbox)
imap.select_folder('INBOX')

# Search for emails from the specific sender
uids = imap.search(['FROM', specific_email_address])

# Loop through the list of email UIDs and fetch each email
for uid in uids:
    raw_email = imap.fetch(uid, ['RFC822'])[uid][b'RFC822'].decode('ISO-8859-1')
    
    # Process or print the email content as needed
    print(raw_email)

# Close the IMAP connection
imap.logout()
