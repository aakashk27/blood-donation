from django.contrib import admin
from backend.models import *

# Register your models here.
admin.site.register(User)
class User(admin.ModelAdmin):
    list_display = ('username', 'email', 'is_donor', 'is_recipient', 'is_admin')


admin.site.register(Profile)
class Profile(admin.ModelAdmin):
    list_display = ('user', 'phone_number', 'date_of_birth', 'address', 'city', 'state', 'country')
    list_select_related = ('user','city')
    search_fields = ('user__username', 'user__email', 'phone_number')
    list_filter = ('city', 'state', 'country')
    list_per_page = 10


admin.site.register(BloodBank)
class BloodBank(admin.ModelAdmin):
    list_display = ('name', 'address', 'city', 'state', 'country', 'email', 'phone_number', 'license_number')
    list_select_related = ('city',)
    search_fields = ('name', 'city__name', 'state', 'country', 'email', 'phone_number', 'license_number')
    list_filter = ('city', 'state', 'country')
    list_per_page = 10