from django.urls import path, include
from rest_framework.routers import DefaultRouter
from backend.BloodBanks.views import BloodBankRegister

router = DefaultRouter()
router.register('banks', BloodBankRegister, basename='user-registration')

urlpatterns = [
    path('api/', include(router.urls)),
]
