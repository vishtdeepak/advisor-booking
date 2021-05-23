from rest_framework import serializers
from .models import *
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import update_last_login



class UserRegistrationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Account
        fields = ('email', 'password', 'name')
        extra_kwargs = {
            'password': {'write_only': True},
            'name': {'required': True}
        }

    def create(self, validated_data):
        user = Account.objects.create_user(
            validated_data['email'], validated_data['name'], validated_data['password']
        )
        # Token.objects.create(user=user)
        return user



class AdvisorBookingSerializer(serializers.ModelSerializer):
    class Meta:
        model =  AdvisorBooking
        fields = "__all__"

# booking_advisor_date = AdvisorBookingSerializer(many=True, read_only=True, required=False)


class AdvisorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Advisor
        fields = "__all__"


class AdvisorSerializerDate(AdvisorSerializer):
    booking_advisor_date = AdvisorBookingSerializer(many=True, read_only=True, required=False)






