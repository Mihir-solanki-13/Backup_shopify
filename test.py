import requests
import json

shop_url = 'quickstart-b4fa8ebd.myshopify.com'
access_token = ''
cli_token = 'atkn_20eaf778ff3ea2aae723595588b7078080228d474e0183414d58600007900682'
# Define the API endpoint URL



def fetch_shopify_data():
    url = f'https://{shop_url}/admin/api/2024-01/products.json'

    # Make the request with the access token included in the headers
    headers = {
        'X-Shopify-Access-Token': access_token,
        'Content-Type': 'application/json'
    }
    response = requests.get(url, headers=headers)
    # url = f'https://{api_key}:{api_password}@{shop_url}/admin/api/202X-XX/{resource}.json'
    # response = requests.get(url)
    data = response.json()
    print(data)
    return data

data = fetch_shopify_data()
