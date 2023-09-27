import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


def mail_sender(subject:"", message_body:""):
    # Your email account information
    sender_email = 'xmpython@zohomail.com'
    sender_password = 'Python2023!'
    
    # Zoho Mail SMTP server settings
    smtp_server = 'smtp.zoho.com'
    smtp_port = 587  # Use 465 if you prefer SSL
    
    # Recipient email address
    recipient_email = 'xmslyz@icloud.com'
    
    message = MIMEMultipart()
    message['From'] = sender_email
    message['To'] = recipient_email
    message['Subject'] = subject
    
    # Email body
    message.attach(MIMEText(message_body, 'plain'))
    
    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(sender_email, sender_password)
        text = message.as_string()
        server.sendmail(sender_email, recipient_email, text)
        server.quit()
        print("Email sent successfully")
    except Exception as e:
        print(f"Email could not be sent. Error: {str(e)}")
    