from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from app import serializers
from app.models import *

# Create your views here.
class Student_detail(APIView):
    serializers_class=serializers.StudentSerializers
    def get(self,request,format=None):
        return Response({'name':'gowthami','message':'hello gowthami'})
    
    def post(self,request,format=None):
        data=self.serializers_class(data=request.data)
        if data.is_valid():
            name=data.validated_data.get('name')
            return Response({'message':"data received {}".format(name)})
        else:
            return Response(data.errors,status=status.HTTP_400_BAD_REQUEST)
    def put(self,request,format=None):
        data=self.serializers_class(data=request.data)
        if data.is_valid():
            name=data.validated_data.get("name")
            return Response({"message":"data patch {}".format(name)})
        else:
            return Response(data.errors,status=status.HTTP_400_BAD_REQUEST)
    def patch(self,request,format=None):
        data=self.serializer_class(data=request.data)
        if data.is_valid():
            name=data.validated_data.get("name")
            return Response({'message':"data patch {}".format(name)})
        else:
            return Response(data.errors,status=status.HTTP_400_BAD_REQUEST)
    def delete(self,request,format=None):
        return Response({'message':"Deleted"})

        
        
class StudentViewset(viewsets.ViewSet):
    serializer_class=serializers.StudentSerializers
    def list(self,request):
        data=Student_details.objects.values()
        d={'data':data}
        return Response(d)

    def create(self,request):
        data=self.serializer_class(data=request.data)
        if data.is_valid():
            name=data.validated_data.get("name")
            return Response({'message':"data recieved {}".format(name)})
        else:
            return Response(data.errors,status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self,request,pk=None):
        return Response({"message":"retrive method is completely similar to GET http method"})

    def update(self,request,pk=None):
        data=self.serializer_class(data=request.data)
        if data.is_valid():
            name=data.validated_data.get("name")
            return Response({'message':"data recieved {}".format(name)})
        else:
            return Response(data.errors,status=status.HTTP_400_BAD_REQUEST)

    def partial_update(self,request,pk=None):
        return Response({'message':"partial update is similar to patch http method "})

    def destroy(self,request,pk=None):
        return Response({'message':"destroy is similar to d elete http method "})
