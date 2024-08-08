from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny

from backend.BloodBanks.serializers import BloodBankRegistrationSerializer



class BloodBankRegister(viewsets.ViewSet):
    permission_classes = [AllowAny]

    def create(self, request):
        serializer = BloodBankRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Blood Bank created successfully'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
	
