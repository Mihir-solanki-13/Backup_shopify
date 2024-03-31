from django.shortcuts import render
from django.http import HttpResponse
from .help import *
# Create your views here.

def fetch_restore(request,object_type,version):
    backup_data(object_type,version)

    return HttpResponse("Data fetched and stored successfully!")

def fetch_restore_id(request,id,object_type,version):
    # print(object_type)
    backup_data_id(object_type,id,version)

    return HttpResponse("Data fetched and stored successfully!")

def retore_data(request, id):
   restore(id)
   return HttpResponse("restored")