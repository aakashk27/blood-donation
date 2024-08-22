from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny

from backend.BloodBanks.serializers import BloodBankRegistrationSerializer, BloodInventorySerializer
from backend.models import BloodBank, BloodInventory



class BloodBank(viewsets.ViewSet):
    permission_classes = [AllowAny]

    def create(self, request):
        serializer = BloodBankRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Blood Bank created successfully'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def list(self, request):

        if(request.query_params.get('city')):
            city = request.query_params.get('city')
            queryset = BloodBank.objects.filter(bank_city=city).select_related('bank_city')
            serializer = BloodBankRegistrationSerializer(queryset, many=True)
            return Response(serializer.data)
        
        elif(request.query_params.get('blood_group')):
            blood_group = request.query_params.get('blood_group')
            print(blood_group)
            queryset = BloodInventory.objects.filter(blood_group=blood_group).select_related('blood_bank')
            print(queryset)
            serializer = BloodInventorySerializer(queryset, many=True)
            return Response(serializer.data)

