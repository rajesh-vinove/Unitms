from rest_framework import serializers
from .models import *
from unitms.utils import *

class JObOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = JObOrder
        fields = [ 'id','name']


class PrimeOverSerializer(serializers.ModelSerializer):

    class Meta:
        model = PrimeMover
        fields = [ 'id','pm_number','brand','driven_by','parks_at']


class DriverSerializer(serializers.ModelSerializer):
    class Meta:
        model = Driver
        fields = ['id','fullname','home_address']


class GetTripSerializer(serializers.Serializer):
    
    id = serializers.CharField(required=False, allow_blank=True,allow_null=True, max_length=100)
    driver = DriverSerializer()
    primemover = PrimeOverSerializer()
    jobOrder = JObOrderSerializer()
    startPoint = serializers.CharField(required=False, allow_blank=True,allow_null=True)
    endPoint = serializers.CharField(required=False, allow_blank=True, allow_null=True)
    planTime = serializers.CharField(required=False, allow_blank=True, allow_null=True)
    planBy = serializers.CharField(required=False, allow_blank=True,allow_null=True)
    tripAcknowledged = serializers.CharField(required=False, allow_blank=True, allow_null=True)
    remarks = serializers.CharField(required=False, allow_blank=True, allow_null=True)
    createdBy = serializers.CharField(required=False, allow_blank=True, allow_null=True)
    createdTime = serializers.CharField(required=False, allow_blank=True,allow_null=True)
    subletTo = serializers.CharField(required=False, allow_blank=True,allow_null=True)

    


class TripSerializer(serializers.ModelSerializer):
    
    id = serializers.CharField(required=False, allow_blank=True, max_length=100)
    driver = serializers.CharField(required=False, allow_blank=True, max_length=100)
    primemover = serializers.CharField(required=False, allow_blank=True, max_length=100)
    jobOrder = serializers.CharField(required=False, allow_blank=True, max_length=100)
    startPoint = serializers.CharField(required=False, allow_blank=True, max_length=100)
    endPoint = serializers.CharField(required=False, allow_blank=True, max_length=100)
    planTime = serializers.CharField(required=False, allow_blank=True, max_length=100)
    planBy = serializers.CharField(required=False, allow_blank=True, max_length=100)
    tripAcknowledged = serializers.CharField(required=False, allow_blank=True, max_length=100)
    remarks = serializers.CharField(required=False, allow_blank=True, max_length=100)

    createdBy = serializers.CharField(required=False, allow_blank=True, max_length=100)
    createdTime = serializers.CharField(required=False, allow_blank=True, max_length=100)
    subletTo = serializers.CharField(required=False, allow_blank=True, max_length=100)

    class Meta:
        model = Trip
        fields = ['id','driver','primemover','jobOrder','startPoint','endPoint','planTime','planBy','tripAcknowledged',
                'remarks','isActive',
                    'isRejected','isRejected','createdBy','createdTime','subletTo']

    
    