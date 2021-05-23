from django.db import router
from django.urls import path
from django.urls.conf import include
from rest_framework import routers
from .views import *

router = routers.DefaultRouter()
router.register(r'users', UserViewSet, basename='UserViewSet')


urlpatterns = [

    path('admin/advisor/', AdvisorAdd.as_view()),
    path('user/<int:pk>/advisor/', AdvisorList.as_view(), name='advior'),
    path('user/<int:pk>/advisor/<int:advisor_pk>/', CreateBooking.as_view(), name='advior_booking'),
    path('user/<int:pk>/advisor/booking/', AdvisorListBooking.as_view()),  # work herte!!!
    path('user/register/', UserRegistrationView.as_view()),
    path('user/login/', LoginAPIView.as_view(), name='login'),
    path('', include(router.urls)),


]