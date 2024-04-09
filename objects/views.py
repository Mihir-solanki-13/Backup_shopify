from django.shortcuts import render
from django.http import HttpResponse
from .help import *
# Create your views here.

def fetch_restore(request,object_type):
    backup_data(object_type)

    return HttpResponse("Data fetched and stored successfully!")

def fetch_restore_id(request,id,object_type):
    # print(object_type)
    backup_data_id(object_type,id)

    return HttpResponse("Data fetched and stored successfully!")

def retore_data(request, id):
   restore(id)
   return HttpResponse("restored")


#
# from rest_framework import viewsets
# from rest_framework.response import Response
# from .models import Store, Object
# from .serializers import StoreSerializer, ObjectSerializer
#
# class StoreViewSet(viewsets.ModelViewSet):
#     queryset = Store.objects.all()
#     serializer_class = StoreSerializer
#
# class ObjectViewSet(viewsets.ModelViewSet):
#     queryset = Object.objects.all()
#     serializer_class = ObjectSerializer
#
#     def retrieve(self, request, pk=None):
#         instance = self.get_object()
#         serializer = self.get_serializer(instance)
#         return Response(serializer.data)