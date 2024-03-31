import requests
import json

shop_url = 'quickstart-b4fa8ebd.myshopify.com'
access_token = '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'
# cli_token = 'atkn_20eaf778ff3ea2aae723595588b7078080228d474e0183414d58600007900682'
# # Define the API endpoint URL


# # #get all product
# # def fetch_shopify_data():
# #     url = f'https://{shop_url}/admin/api/2024-01/products.json'

# #     # Make the request with the access token included in the headers
# #     headers = {
# #         'X-Shopify-Access-Token': access_token,
# #         'Content-Type': 'application/json'
# #     }
# #     response = requests.get(url, headers=headers)
# #     # url = f'https://{api_key}:{api_password}@{shop_url}/admin/api/202X-XX/{resource}.json'
# #     # response = requests.get(url)
# #     data = response.json()
# #     print(data)
# #     return data

# # # data = fetch_shopify_data()


# # get a particular product
# id = 9075575652634


# def get_product_withid():
#     # Define the necessary parameters
#     url =  f'https://{shop_url}/admin/api/2024-01/products/{id}.json'
     
    
#     # Define the query parameters
    
#     # Define headers
#     headers = {
#         "X-Shopify-Access-Token": access_token
#     }
    
#     # Make the GET request
#     response = requests.get(url, headers=headers)
#     print(response.status_code)
#     # Check if the request was successful
#     if response.status_code == 200:
#         # Parse JSON response and process the data as needed
#         data = response.json()
#         # Process the data...
        
#         print({'message': 'Data retrieved successfully.', 'data': data})
#     else:
#          print({'error': 'Failed to fetch data from the server.'}, status=response.status_code)

      
# data = {'product': {'id': 9075575652634, 'title': 'Tshirt', 'body_html': 'White tshirt', 'vendor': 'Quickstart (b4fa8ebd)', 'product_type': '', 'created_at': '2024-03-30T03:03:31-04:00', 'handle': 'tshirt', 'updated_at': '2024-03-30T03:03:34-04:00', 'published_at': '2024-03-30T03:03:31-04:00', 'template_suffix': '', 'published_scope': 'global', 'tags': '', 'status': 'active', 'admin_graphql_api_id': 'gid://shopify/Product/9075575652634', 'variants': [{'id': 48214708191514, 'product_id': 9075575652634, 'title': 'Default Title', 'price': '4586.00', 'sku': 'ab.com', 'position': 2, 'inventory_policy': 'deny', 'compare_at_price': None, 'fulfillment_service': 'manual', 'inventory_management': 'shopify', 'option1': 'Default Title', 'option2': None, 'option3': None, 'created_at': '2024-03-30T03:03:32-04:00', 'updated_at': '2024-03-30T03:03:32-04:00', 'taxable': True, 'barcode': '', 'grams': 0, 'weight': 0.0, 'weight_unit': 'kg', 'inventory_item_id': 50261410382106, 'inventory_quantity': 0, 'old_inventory_quantity': 0, 'requires_shipping': True, 'admin_graphql_api_id': 'gid://shopify/ProductVariant/48214708191514', 'image_id': None}], 'options': [{'id': 11404283773210, 'product_id': 9075575652634, 'name': 'Title', 'position': 1, 'values': ['Default Title']}], 'images': [{'id': 45039611707674, 'alt': None, 'position': 1, 'product_id': 9075575652634, 'created_at': '2024-03-30T03:03:31-04:00', 'updated_at': '2024-03-30T03:03:33-04:00', 'admin_graphql_api_id': 'gid://shopify/ProductImage/45039611707674', 'width': 194, 'height': 138, 'src': 'https://cdn.shopify.com/s/files/1/0868/4381/8266/files/download.jpg?v=1711782213', 'variant_ids': []}], 'image': {'id': 45039611707674, 'alt': None, 'position': 1, 'product_id': 9075575652634, 'created_at': '2024-03-30T03:03:31-04:00', 'updated_at': '2024-03-30T03:03:33-04:00', 'admin_graphql_api_id': 'gid://shopify/ProductImage/45039611707674', 'width': 194, 'height': 138, 'src': 'https://cdn.shopify.com/s/files/1/0868/4381/8266/files/download.jpg?v=1711782213', 'variant_ids': []}}}
# id = 9075575652634
# def restore_shopify_data():
    
#     # val = data['product']['id']
    
#     url = f'https://{shop_url}/admin/api/2024-01/products/{id}.json'
#     # print(val)
#     headers = {
#         'X-Shopify-Access-Token': access_token,
#         'Content-Type': 'application/json',
#         'Accept': 'application/json'
#     }
#     response = requests.put(url, headers=headers, data=json.dumps(data))
#     print(response.status_code,response.text)
#     return response

# restore_shopify_data()



#  theme 

# def backup_data(object):
#     url = f'https://{shop_url}/admin/api/2023-10/{object}.json'

#     # Make the request with the access token included in the headers
#     headers = {
#         'X-Shopify-Access-Token': access_token,
#          'Content-Type': 'application/json',
#     }

#     response = requests.get(url, headers=headers)
#     print(response.status_code,response.text)
#     data = response.json()
#     # print(data)
#     # new_instance = Object(
#     # store=store_instances,  # Replace your_store_instance with the actual Store instance
#     # object_type=object,  # Assuming the object_type is "product"
#     # data=data,  # Replace data with your actual JSON data
#     # version=uuid.uuid4(),  # Generate a UUID for the version
#     # backup_date=timezone.now().date()  # Set the backup_date to the current date/time
#     # )

#     # new_instance.save()

# backup_data('themes')

# restore theme by id 



def create_product(data,version):
    url = f'https://{shop_url}/admin/api/{version}/{object}.json'
    headers = {
        "X-Shopify-Access-Token": access_token,
        "Content-Type": "application/json"
    }
   
    response = requests.post(url, json=data, headers=headers)

    print(response.status_code)
    print(response.json())


def restore_shopify_data(resource , data,version):
    url = f'https://{shop_url}/admin/api/{version}/{object}/{data["product"]["id"]}.json'
    headers = {
        'X-Shopify-Access-Token': access_token,
        'Content-Type': 'application/json',
        'Accept': 'application/json'
    }
    response = requests.put(url, headers=headers, data=json.dumps(data))
    
    return response

def restore(id):
    Obj = Object.objects.get(version=id)
    products = Obj.data
    for product in products['products']:
        response = restore_shopify_data('products', {'product': product})
        # print(response.status_code)
        if response.status_code != 200:
             print('creating product')
            #  print(product)
             create_product({'product': product})
    # print(data)
    