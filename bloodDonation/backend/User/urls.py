from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BloodDonationRequest, CompleteBloodDonationRequest, UserRegistrationViewSet, UserLoginViewSet, UserProfileViewSet
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

router = DefaultRouter()
router.register('register', UserRegistrationViewSet, basename='user-registration')
router.register('login', UserLoginViewSet, basename='user-login')
router.register('profile', UserProfileViewSet, basename='user-profile')
router.register('donation-request', BloodDonationRequest, basename='donation-request')
router.register('complete-donation-request', CompleteBloodDonationRequest, basename='complete-donation-request')

urlpatterns = [
    path('api/', include(router.urls)),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
