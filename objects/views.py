from django.shortcuts import render
from django.http import HttpResponse
from .help import *
# Create your views here.

def fetch_restore(request,store_id,object_type):
    backup_data(object_type)

    return HttpResponse("Data fetched and stored successfully!")

def fetch_restore_id(request,id,object_type):
    print(object_type)
    backup_data_id(object_type,id)

    return HttpResponse("Data fetched and stored successfully!")

def retore_data(request, id):
   restore(id)
   return HttpResponse("restored")