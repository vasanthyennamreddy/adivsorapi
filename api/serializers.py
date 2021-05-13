from django.db.models import fields
from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User

class RegistrationSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['username','email','password']


class AdivsorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Advisor
        fields = '__all__'

class CallSerializer(serializers.ModelSerializer):
    class Meta:
        model = Call
        fields = '__all__'

class BookingSerializer(serializers.Serializer):
    booking_id = serializers.IntegerField()
    adv_id = serializers.IntegerField()
    adv_name = serializers.CharField(max_length=50)
    adv_pic = serializers.CharField(max_length= 100)
    time = serializers.DateTimeField()
