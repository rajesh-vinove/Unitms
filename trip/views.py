from django.shortcuts import render

from .serializers import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import (
    AllowAny,
)
from rest_framework.renderers import JSONRenderer
from rest_framework import exceptions
from unitms.userpermission import *

class AddTrip(APIView):
    """
    All permissions  are maitained from userpermission.
    """
    permission_classes = [AdminBaseUser]
    def post(self, request):
        
        data = request.data
        serializer = TripSerializer(data=data)
        if serializer.is_valid():
            try:
                job_order_obj = JObOrder.objects.get(id=data['jobOrder'])
            except JObOrder.DoesNotExist:
                raise CustomValidationError(detail="Invalid Job Order Id.")

            trip_obj = Trip.objects.create(jobOrder = job_order_obj, startPoint = data['startPoint'], 
                                    endPoint = data['endPoint'],remarks = data['remarks'],
                                    createdBy=data['createdBy'])

            trip_data = GetTripSerializer(trip_obj)
            return Response(trip_data.data, status=201)
        return Response(serializer.data, status=400)

class GetTripDetails(APIView):
    permission_classes = [AllowAny]
    def get(self, request):
        data = request.query_params
        try:
            trip_obj = Trip.objects.get(id=data['id'])
            serializer = GetTripSerializer(trip_obj)
        except Trip.DoesNotExist:
            raise exceptions.NotFound(detail="Trip is not found by this id.") 
        return Response(serializer.data, status=200)

class GetTripList(APIView):
    permission_classes = [AdminBaseUser]
    def get(self, request):
        data = request.query_params
        trip_obj = Trip.objects.filter(primemover__id=data['primemover_id'])
        serializer = GetTripSerializer(trip_obj,many=True)
        return Response(serializer.data, status=200)
        
class DeleteTrip(APIView):
    permission_classes = [AdminUser]
    def delete(self,request):
        data = request.query_params
        try:
            trip_obj = Trip.objects.get(id=data['trip_id'])
            trip_obj.delete()
        except Trip.DoesNotExist:
            raise exceptions.NotFound(detail="Trip is not found by this id.") 
        return Response({}, status=202)

class UpdateTrip(APIView):
    permission_classes = [AllowAny]
    def put(self,request):
        data = request.data
        serializer = TripSerializer(data=data)
        if serializer.is_valid():
            try:
                Trip.objects.filter(id=request.query_params['id']).update(**data)
                trip_updated_obj = Trip.objects.get(id=request.query_params['id'])
                serializer = GetTripSerializer(trip_updated_obj)
                return Response(serializer.data, status=200)
            except Trip.DoesNotExist:
                raise exceptions.NotFound(detail="Trip is not found by this id.")     
        else:
            return Response(serializer.data, status=400)
        

