import smtplib

smtp_server = 'smtp.gmail.com'  # Replace with your SMTP server address
smtp_port = 587  # Replace with your SMTP port number
smtp_username = 'ftd10622564@desu.ac.in'  # Replace with your SMTP username
smtp_password = 'SHUBH@DSEU8936'  # Replace with your SMTP password

try:
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()
    server.login(smtp_username, smtp_password)
    print("SMTP connection successful")
    server.quit()
except Exception as e:
    print("SMTP connection failed:", e)
