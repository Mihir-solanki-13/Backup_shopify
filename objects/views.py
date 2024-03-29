from django.shortcuts import render
from django.http import HttpResponse
from .help import *
# Create your views here.

def fetch_restore(request):
    backup_data('product')

    return HttpResponse("Data fetched and stored successfully!")

def retore_data(request, id):
   restore(id)
   return HttpResponse("restored")