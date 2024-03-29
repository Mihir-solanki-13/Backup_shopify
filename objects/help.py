import uuid
import requests
import json

from django.utils import timezone
from .models import *


shop_url = 'quickstart-b4fa8ebd.myshopify.com'
access_token = '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' 
# Define the API endpoint URL
 
store_instances = Store.objects.get(organization_name="Mihir")

def backup_data(object):
    url = f'https://{shop_url}/admin/api/2024-01/{object}.json'

    # Make the request with the access token included in the headers
    headers = {
        'X-Shopify-Access-Token': access_token,
        'Content-Type': 'application/json'
    }

    response = requests.get(url, headers=headers)
    data = response.json()
    # print(data)
    new_instance = Object(
    store=store_instances,  # Replace your_store_instance with the actual Store instance
    object_type=object,  # Assuming the object_type is "product"
    data=data,  # Replace data with your actual JSON data
    version=uuid.uuid4(),  # Generate a UUID for the version
    backup_date=timezone.now().date()  # Set the backup_date to the current date/time
    )

    new_instance.save()


def restore_shopify_data(data):
    url = f'https://{shop_url}/admin/api/2024-01/products/{data["product"]["id"]}.json'
    headers = {
        'X-Shopify-Access-Token': access_token,
        'Content-Type': 'application/json',
        'Accept': 'application/json'
    }
    response = requests.put(url, headers=headers, data=json.dumps(data))
    print(response.status_code)
    return response

def restore(id):
    Obj = Object.objects.get(version=id)
    products = Obj.data
    for product in products['products']:
        response = restore_shopify_data('products', {'product': product})

        if response.status_code != 200:
            print(f"Error restoring product: {response.text}") 
    # print(data)
    