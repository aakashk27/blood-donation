from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import ListModelMixin, CreateModelMixin

class UserRegistration(GenericViewSet, ListModelMixin, CreateModelMixin):
    
    def post(self, request):
        pass
