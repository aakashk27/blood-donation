from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    is_donor = models.BooleanField(default=False)
    is_recipient = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)

User._meta.get_field('groups').remote_field.related_name = 'user_group_set'
User._meta.get_field('user_permissions').remote_field.related_name = 'user_permission_set'


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=15)
    date_of_birth = models.DateField()
    address = models.TextField(max_length=255, blank=True)
    city = models.ForeignKey('City', on_delete=models.CASCADE)
    state = models.CharField(max_length=100)
    country = models.CharField(max_length=100)


class BloodDonor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    blood_group = models.CharField(max_length=5)
    availability = models.BooleanField(default=True)
    last_donation_date = models.DateField(null=True, blank=True)


class BloodBank(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=255)
    city = models.ForeignKey('City', on_delete=models.CASCADE)
    state = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    license_number = models.CharField(max_length=50)


class DonationRequest(models.Model):
    requested_by = models.ForeignKey(User, on_delete=models.CASCADE)
    blood_group = models.CharField(max_length=5)
    quantity = models.IntegerField()
    location = models.CharField(max_length=255)
    status = models.CharField(max_length=20, default='pending')
    creation_date = models.DateField(auto_now_add=True)
    fulfillment_date = models.DateField(null=True, blank=True)


class DonationHistory(models.Model):
    donor = models.ForeignKey(BloodDonor, on_delete=models.CASCADE)
    date_of_donation = models.DateField()
    quantity = models.IntegerField()
    receiving_bank = models.ForeignKey(BloodBank, on_delete=models.CASCADE)


class City(models.Model):
    name = models.CharField(max_length=255)
    pincode = models.CharField(max_length=255, blank=True)
