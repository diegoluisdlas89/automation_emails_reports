import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import json

class EmailHandler:
    def __init__(self, config_dir):
        with open(f"{config_dir}/email_config.json", 'r') as file:
            self.config = json.load(file)

    def send_email_with_attachment(self, to, subject, body, attachment_path):
        msg = MIMEMultipart()
        msg['From'] = self.config['sender_email']
        msg['To'] = ', '.join(to)
        msg['Subject'] = subject

        msg.attach(MIMEText(body, 'plain'))

        with open(attachment_path, 'rb') as attachment:
            part = MIMEBase('application', 'octet-stream')
            part.set_payload(attachment.read())
            encoders.encode_base64(part)
            part.add_header('Content-Disposition', f"attachment; filename={attachment_path.split('/')[-1]}")
            msg.attach(part)

        with smtplib.SMTP(self.config['smtp_server'], self.config['smtp_port']) as server:
            server.starttls()
            server.login(self.config['sender_email'], self.config['password'])
            server.send_message(msg)