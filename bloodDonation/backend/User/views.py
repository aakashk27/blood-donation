# views.py
import datetime
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from backend.User.serializers import ProfileSerializer, RequestBloodDonationSerializer, UserLoginSerializer, UserRegistrationSerializer
from backend.models import BloodDonor, CompleteDonationRequest, DonationRequest, Profile

import logging

logger = logging.getLogger(__name__)

class UserRegistrationViewSet(viewsets.ViewSet):
    permission_classes = [AllowAny]

    def create(self, request):
        serializer = UserRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                'message': 'User created successfully',
                }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserLoginViewSet(viewsets.ViewSet):
    permission_classes = [AllowAny]

    def create(self, request):
        serializer = UserLoginSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data['user']
            user_profile = Profile.objects.get(user=user)
            refresh = RefreshToken.for_user(user)
            return Response({
                'refresh': str(refresh),
                'access': str(refresh.access_token),
                'user': user.id,
                'user_profile': user_profile.id
            }, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class UserProfileViewSet(viewsets.ViewSet):
    permission_classes = [IsAuthenticated]

    def retrieve(self, request, pk=None):
        try:
            profile = Profile.objects.get(pk=pk)
            serializer = ProfileSerializer(profile)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Profile.DoesNotExist:
            return Response({'error': 'Profile not found'}, status=status.HTTP_404_NOT_FOUND)
            
    def partial_update(self, request, pk=None):
        try:
            profile = Profile.objects.get(pk=pk)
            serializer = ProfileSerializer(profile, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Profile.DoesNotExist:
            return Response({'error': 'Profile not found'}, status=status.HTTP_404_NOT_FOUND)


class BloodDonationRequest(viewsets.ViewSet):

    def create(self, request):
        serializer = RequestBloodDonationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        

class CompleteBloodDonationRequest(viewsets.ViewSet):

    def create(self, request):
        donor_id = request.data.get('donor_id')
        blood_group = request.data.get('blood_group')
        quantity = request.data.get('quantity')
        donation_request_id = request.data.get('donation_request_id')

        try:
            donation_request = DonationRequest.objects.get(pk=donation_request_id)
            donor = BloodDonor.objects.get(pk=donor_id, blood_group=blood_group, availability=True)

            if donation_request.blood_group == blood_group and donation_request.quantity == quantity:
                donation_request.status = 'fulfilled'
                donation_request.fulfillment_date = datetime.datetime.now()
                donation_request.save(update_fields=['status'])

                CompleteDonationRequest.objects.create(
                    requested_by=donation_request, 
                    donor=donor, 
                    quantity=quantity
                )
                
                return Response({'message': 'Donation request fulfilled'}, status=status.HTTP_200_OK)
            return Response({'error': 'Donation request not fulfilled'}, status=status.HTTP_400_BAD_REQUEST)
        except DonationRequest.DoesNotExist:
            return Response({'error': 'Donation request not found'}, status=status.HTTP_404_NOT_FOUND)
        except BloodDonor.DoesNotExist:
            return Response({'error': 'Donor not found'}, status=status.HTTP_404_NOT_FOUND)
        


    
