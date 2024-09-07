from django.contrib import admin
from backend.models import *

# Register your models here.
@admin.register(User)
class User(admin.ModelAdmin):
    list_display = ('username', 'email', 'is_donor', 'is_recipient', 'is_admin')


@admin.register(Profile)
class Profile(admin.ModelAdmin):
    list_display = ('user', 'phone_number', 'date_of_birth', 'address', 'user_city', 'state', 'country')
    list_select_related = ('user', 'user_city')
    search_fields = ('user__username', 'user__email', 'phone_number')
    list_filter = ('user_city', 'state', 'country')
    list_per_page = 10


@admin.register(BloodBank)
class BloodBank(admin.ModelAdmin):
    list_display = ('name', 'address', 'bank_city')
    list_select_related = ('bank_city',)
    search_fields = ('name',)
    list_filter = ('name', 'state', 'country', 'bank_city')
    list_per_page = 10

@admin.register(City)
class City(admin.ModelAdmin):
    list_display = ('name', 'pincode')
    list_filter = ('name', )
    search_fields = ('name', 'pincode')
    list_per_page = 10


@admin.register(BloodInventory)
class BloodInventory(admin.ModelAdmin):
    list_display = ('blood_bank', 'blood_group', 'quantity')
    list_select_related = ('blood_bank',)
    search_fields = ('blood_bank__name', 'blood_group')
    list_filter = ('quantity', )
    list_per_page = 10


@admin.register(BloodDonor)
class BloodDonor(admin.ModelAdmin):
    list_display = ('user', 'blood_group', 'availability', 'last_donation_date')
    list_select_related = ('user',)
    search_fields = ('user__username', 'user__email', 'blood_group')
    list_filter = ('blood_group', 'availability', 'last_donation_date')
    list_per_page = 10


@admin.register(DonationRequest)
class DonationRequest(admin.ModelAdmin):
    list_display = ('requested_by', 'blood_group', 'quantity', 'location', 'status', 'creation_date', 'fulfillment_date')
    list_select_related = ('requested_by',)
    search_fields = ('requested_by__username', 'requested_by__email', 'location')
    list_filter = ('status', 'creation_date', 'fulfillment_date')
    list_per_page = 10
