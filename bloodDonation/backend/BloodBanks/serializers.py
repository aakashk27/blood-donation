from rest_framework import serializers
from backend.models import BloodBank, BloodInventory


class BloodBankRegistrationSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = BloodBank
        fields = '__all__'

class BloodInventorySerializer(serializers.ModelSerializer):
    blood_bank = serializers.CharField(source='blood_bank.name')

    class Meta:
        model = BloodInventory
        fields = ['blood_bank', 'blood_group', 'quantity']
