from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny

from backend.BloodBanks.serializers import BloodBankRegistrationSerializer
from backend.models import BloodBank



class BloodBankRegister(viewsets.ViewSet):
    permission_classes = [AllowAny]

    def create(self, request):
        serializer = BloodBankRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Blood Bank created successfully'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def list(self, request):
        city = request.query_params.get('city')
        print(city)
        if city:
            queryset = BloodBank.objects.filter(bank_city=city).select_related('bank_city')
        else:
            queryset = BloodBank.objects.all()
        serializer = BloodBankRegistrationSerializer(queryset, many=True)
        return Response(serializer.data)

