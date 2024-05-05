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
    
    
def object_detail(request,object_type,id):
    # product_data = Object.objects.filter(object_type=object_type).values('data')c
    # product_data = Object.objects.filter(object_type=object_type).values('data')
    object_data = Object.objects.filter(object_type=object_type).values('data','backup_date','uuid')
     

# List to store the filtered products
    filtered_objects= []

# Iterate through each dictionary in the queryset
    for data_item in object_data:
        # Access the 'products' list from the 'data' key
        obj = data_item.get('data', {}).get(object_type, [])
        # Iterate through each product in the list
        for object in obj:
            # Check if the product title matches the target title
            if object.get('id') == id:
                # If it matches, add it to the filtered list
                # object['backup_date'] = data_item['backup_date']
                object['backup_date'] = data_item['backup_date'].strftime("%Y-%m-%d %H:%M:%S")
                object['uuid'] = str(data_item['uuid'])
                filtered_objects.append(object)

    # Print the filtered products
    # print(filtered_objects)
    return JsonResponse(filtered_objects,safe=False)
        
def get_curr_object(request,object_type,id):
    
    json_data = get_object_by_id(object_type,id)
    return JsonResponse(json_data,safe=False)

def bulk_backup(request):
    for object_type, _ in OBJECT_TYPES:
        backup_data(object_type)
    
    response_data = {'message': 'Bulk backup success'}
     
    # Return JSON response with the success message
    return JsonResponse(response_data,safe=False)

def restore_by_id(request, uuid, objectType, id):
     
    restore_id(request,uuid,objectType,id)
    response_data = {'success': True, 'uuid': uuid, 'objectType': objectType, 'id': id}
    return JsonResponse(response_data)

   