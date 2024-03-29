# fetch_product.py
import requests
import json
from django.http import HttpResponse
from django.utils import timezone
from .models import MyModel  # Replace 'myapp' with the name of your Django app

shop_url = 'quickstart-b4fa8ebd.myshopify.com'
access_token = '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'
cli_token = 'atkn_20eaf778ff3ea2aae723595588b7078080228d474e0183414d58600007900682'
# Define the API endpoint URL

def fetch_shopify_data(request):
    url = f'https://{shop_url}/admin/api/2024-01/products.json'

    # Make the request with the access token included in the headers
    headers = {
        'X-Shopify-Access-Token': access_token,
        'Content-Type': 'application/json'
    }
    response = requests.get(url, headers=headers)
    data = response.json()

    parsed_data = data

    for product_data in parsed_data['products']:
        product_id = str(product_data['id'])
        version = '1.0'

        my_model_instance = MyModel.objects.create(
            product_id=product_id,
            json_data=product_data,
            version=version,
            created_at=timezone.now()
        )
        my_model_instance.save()

    return HttpResponse("Data fetched and stored successfully!")
