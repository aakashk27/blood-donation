from rest_framework import serializers
from django.contrib.auth import authenticate
from backend.models import DonationRequest, Profile, User


class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = '__all__'

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
            is_donor=validated_data.get('is_donor', False),
            is_recipient=validated_data.get('is_recipient', False)
        )
        user.set_password(validated_data['password'])
        user.save()

        user_profile=Profile.objects.create(user=user)

        return user_profile


class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        username = data.get('username')
        password = data.get('password')

        if username and password:
            user = authenticate(username=username, password=password)
            if user:
                data['user'] = user
            else:
                raise serializers.ValidationError("Invalid credentials")
        else:
            raise serializers.ValidationError("Must include both username and password")

        return data


class ProfileSerializer(serializers.ModelSerializer):

    class Meta:
       model = Profile
       fields = '__all__'
       read_only = ['user']


class RequestBloodDonationSerializer(serializers.ModelSerializer):

    class Meta:
        model = DonationRequest
        fields = '__all__'
        read_only = ['user']
