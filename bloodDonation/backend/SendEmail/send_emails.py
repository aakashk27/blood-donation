import sendinblue
from sendinblue import SMTP
from django.conf import settings

def send_email_to_donors(donor_emails, subject, message):
    smtp_client = SMTP(settings.SENDINBLUE_API_KEY)
    data = {
        'sender': {'name': 'Blood Donation', 'email': 'xxxxxxxx'},
        'to': [{'email': email} for email in donor_emails],
        'subject': subject,
        'htmlContent': message
    }
    response = smtp_client.send_transactional_email(data)
    return response
