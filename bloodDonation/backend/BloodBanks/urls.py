from django.urls import path, include
from rest_framework.routers import DefaultRouter
from backend.BloodBanks.views import BloodBank

router = DefaultRouter()
router.register('banks', BloodBank, basename='user-registration')

urlpatterns = [
    path('api/', include(router.urls)),
]
