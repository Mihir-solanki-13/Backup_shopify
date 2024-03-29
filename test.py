import requests
import json

shop_url = 'quickstart-b4fa8ebd.myshopify.com'
access_token = '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'
cli_token = 'atkn_20eaf778ff3ea2aae723595588b7078080228d474e0183414d58600007900682'
# Define the API endpoint URL


#get all product
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

# data = fetch_shopify_data()


# get a particular product
id = 9067311923482


def get_product_withid():
    # Define the necessary parameters
    url =  f'https://{shop_url}/admin/api/2024-01/products/{id}.json'
     
    
    # Define the query parameters
    
    # Define headers
    headers = {
        "X-Shopify-Access-Token": access_token
    }
    
    # Make the GET request
    response = requests.get(url, headers=headers)
    
    # Check if the request was successful
    if response.status_code == 200:
        # Parse JSON response and process the data as needed
        data = response.json()
        # Process the data...
        
        print({'message': 'Data retrieved successfully.', 'data': data})
    else:
         print({'error': 'Failed to fetch data from the server.'}, status=response.status_code)

data = get_product_withid()