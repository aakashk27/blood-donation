from rest_framework import serializers
from backend.models import BloodBank


class BloodBankRegistrationSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = BloodBank
        fields = '__all__'