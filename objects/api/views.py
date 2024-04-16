from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.db.models import Count
from ..models import *
from django.http import JsonResponse
from ..help import *

def get_object_type_counts(request):
    # Initialize type_counts with counts of 0 for all object types
    type_counts = {object_type: 0 for object_type, _ in OBJECT_TYPES}
    
    # Query the database to get counts for each object type
    counts = Object.objects.values('object_type').filter(object_type__in=type_counts).annotate(count=Count('object_type'))
    
    # Update the counts in the dictionary
    for item in counts:
        object_type = item['object_type']
        count = item['count']
        type_counts[object_type] = count
    
    return JsonResponse(type_counts)


def object_list(request, object_type):
    # print(object_type)
    json_data = get_object(object_type)
    object_list = []

    # Loop through each product in the JSON data and extract ID and title
    obj = object_type[:-1]
    for obj in json_data.get(object_type, []):
        id = obj.get('id')
        title = obj.get('title') or obj.get('name')
        if id and title:
            product_dict = {'id': id, 'title': title}
            object_list.append(product_dict)
            
    return JsonResponse(object_list,safe=False)
    
    