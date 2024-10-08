
from django.db.models.signals import post_save
from django.dispatch import receiver
from requests import Response

from bloodDonation.backend.SendEmail.send_emails import send_email_to_donors
from bloodDonation.backend.models import BloodDonor, DonationRequest


@receiver(post_save, sender=DonationRequest, dispatch_uid='send_emails')
def update_donation_request(sender, instance, **kwargs):
    donor  = BloodDonor.objects.filter(blood_group=instance.blood_group, availability=True)
    donor_emails = [donor.user.email for donor in donor]

    subject = 'New Blood Donation Request'
    message = '<p>A new blood donation request has been created. Please consider donating.</p>'
    
    # Send email to donors
    send_email_to_donors(donor_emails, subject, message)
    print('New blood donation request has been created. Email will be sent')
    