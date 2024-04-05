import requests
import json

shop_url = 'quickstart-b4fa8ebd.myshopify.com'
access_token = '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'
cli_token = 'atkn_20eaf778ff3ea2aae723595588b7078080228d474e0183414d58600007900682'
# Define the API endpoint URL


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

def backup_data(object):
    url = f'https://{shop_url}//admin/api/2024-04/orders/5916810379546/metafields.json'

    
    # Make the request with the access token included in the headers
    headers = {
        'X-Shopify-Access-Token': access_token,
         
    }

    response = requests.get(url, headers=headers)
    print(response.status_code,response.text)
    data = response.json()

backup_data('orders')
    # print(data)
    # new_instance = Object(
    # store=store_instances,  # Replace your_store_instance with the actual Store instance
    # object_type=object,  # Assuming the object_type is "product"
    # data=data,  # Replace data with your actual JSON data
    # version=uuid.uuid4(),  # Generate a UUID for the version
    # backup_date=timezone.now().date()  # Set the backup_date to the current date/time
    # )

    # new_instance.save()

# backup_data('themes')

# restore theme by id 



# def create_product(data,version):
#     url = f'https://{shop_url}/admin/api/{version}/{object}.json'
#     headers = {
#         "X-Shopify-Access-Token": access_token,
#         "Content-Type": "application/json"
#     }
   
#     response = requests.post(url, json=data, headers=headers)

#     print(response.status_code)
#     print(response.json())


# def restore_shopify_data(resource , data,version):
#     url = f'https://{shop_url}/admin/api/{version}/{object}/{data["product"]["id"]}.json'
#     headers = {
#         'X-Shopify-Access-Token': access_token,
#         'Content-Type': 'application/json',
#         'Accept': 'application/json'
#     }
#     response = requests.put(url, headers=headers, data=json.dumps(data))
    
#     return response
# data = {'customer':   'first_name': 'Russell', 'last_name': 'Winfield', 'company': 'Company Name', 'address1': '105 Victoria St', 'address2': None, 'city': 'Toronto', 'province': None, 'country': 'Canada', 'zip': 'M5C1N7', 'phone': None, 'name': 'Russell Winfield', 'province_code': None, 'country_code': 'CA', 'country_name': 'Canada', 'default': True}], 'tax_exemptions': [], 'email_marketing_consent': {'state': 'not_subscribed', 'opt_in_level': 'single_opt_in', 'consent_updated_at': None}, 'sms_marketing_consent': {'state': 'not_subscribed', 'opt_in_level': 'single_opt_in', 'consent_updated_at': None, 'consent_collected_from': 'OTHER'}, 'admin_graphql_api_id': 'gid://shopify/Customer/7971955245338', 'default_address': {'id': 9957007098138, 'customer_id': 7971955245338, 'first_name': 'Russell', 'last_name': 'Winfield', 'company': 'Company Name', 'address1': '105 Victoria St', 'address2': None, 'city': 'Toronto', 'province': None, 'country': 'Canada', 'zip': 'M5C1N7', 'phone': None, 'name': 'Russell Winfield', 'province_code': None, 'country_code': 'CA', 'country_name': 'Canada', 'default': True}}}
# data = '{"customer":{"first_name":"Steve","last_name":"Lastnameson","email":"steve.lastnameson@example.com","phone":"+15142546011","verified_email":true,"addresses":[{"address1":"123 Oak St","city":"Ottawa","province":"ON","phone":"555-1212","zip":"123 ABC","last_name":"Lastnameson","first_name":"Mother","country":"CA"}],"password":"newpass","password_confirmation":"newpass","send_email_welcome":false}}'
# data = {
#     "customer": {
#         "first_name": "kbc",
#         "last_name": "Lastnameson",
#         "email": "steve.tnameson@example.com",
#         "phone": "+15142549011",
#         "verified_email": True,
#         "addresses": [
#             {
#                 "address1": "123 Oak St",
#                 "city": "Ottawa",
#                 "province": "ON",
#                 "phone": "555-1212",
#                 "zip": "123 ABC",
#                 "last_name": "Lastnameson",
#                 "first_name": "Mother",
#                 "country": "CA"
#             }
#         ],
#         "password": "newpass",
#         "password_confirmation": "newpass",
#         "send_email_welcome": False
#     }
# }

# def create_obj(object_type,data):
#     url = f'https://{shop_url}/admin/api/2024-01/customers.json'
#     headers = {
#         "X-Shopify-Access-Token": access_token,
#         "Content-Type": "application/json"
#     }
#     print(data)
#     response = requests.post(url, json=data, headers=headers)

#     print(response.status_code,response.text)
#     print(response.json())

# create_obj('customers',data)

# import requests
# da = {"order": {"id": 5916780364058, "line_items": [{"id": 15075125264666, "admin_graphql_api_id": "gid://shopify/LineItem/15075125264666", "current_quantity": 1, "fulfillable_quantity": 1, "fulfillment_service": "manual", "fulfillment_status": null, "gift_card": false, "grams": 0, "name": "The Collection Snowboard: Hydrogen", "price": "600.00", "price_set": {"shop_money": {"amount": "600.00", "currency_code": "INR"}, "presentment_money": {"amount": "600.00", "currency_code": "INR"}}, "product_exists": true, "product_id": 9088415465754, "properties": [], "quantity": 1, "requires_shipping": true, "sku": "", "taxable": true, "title": "The Collection Snowboard: Hydrogen", "total_discount": "0.00", "total_discount_set": {"shop_money": {"amount": "0.00", "currency_code": "INR"}, "presentment_money": {"amount": "0.00", "currency_code": "INR"}}, "variant_id": 48266826055962, "variant_inventory_management": "shopify", "variant_title": null, "vendor": "Hydrogen Vendor", "tax_lines": [{"channel_liable": false, "price": "54.00", "price_set": {"shop_money": {"amount": "54.00", "currency_code": "INR"}, "presentment_money": {"amount": "54.00", "currency_code": "INR"}}, "rate": 0.09, "title": "CGST"}], "duties": [], "discount_allocations": []}, {"id": 15075125297434, "admin_graphql_api_id": "gid://shopify/LineItem/15075125297434", "current_quantity": 1, "fulfillable_quantity": 1, "fulfillment_service": "manual", "fulfillment_status": null, "gift_card": false, "grams": 0, "name": "The Collection Snowboard: Liquid", "price": "749.95", "price_set": {"shop_money": {"amount": "749.95", "currency_code": "INR"}, "presentment_money": {"amount": "749.95", "currency_code": "INR"}}, "product_exists": true, "product_id": 9088415531290, "properties": [], "quantity": 1, "requires_shipping": true, "sku": "", "taxable": true, "title": "The Collection Snowboard: Liquid", "total_discount": "0.00", "total_discount_set": {"shop_money": {"amount": "0.00", "currency_code": "INR"}, "presentment_money": {"amount": "0.00", "currency_code": "INR"}}, "variant_id": 48266826121498, "variant_inventory_management": "shopify", "variant_title": null, "vendor": "Hydrogen Vendor", "tax_lines": [{"channel_liable": false, "price": "67.50", "price_set": {"shop_money": {"amount": "67.50", "currency_code": "INR"}, "presentment_money": {"amount": "67.50", "currency_code": "INR"}}, "rate": 0.09, "title": "CGST"}], "duties": [], "discount_allocations": []}]}}
# print(type(da))
# data_dict = json.loads(da)
# # dat_dict = json.loads(json_str)
# dat = da.get('order')
# print(dat)
# line_items = dat['order'].get('line_items')
# transactions = dat['order'].get('transactions')
# data = {'order': {'line_items': line_items, 'transactions': transactions}}

# data = {
#     "order": {
#         "line_items": [
#             {
#                 "title": "Big Brown Bear Boots",
#                 "price": 74.99,
#                 "grams": "1300",
#                 "quantity": 3,
#                 "tax_lines": [
#                     {
#                         "price": 13.5,
#                         "rate": 0.06,
#                         "title": "State tax"
#                     }
#                 ]
#             }
#         ],
#         "transactions": [
#             {
#                 "kind": "sale",
#                 "status": "success",
#                 "amount": 238.47
#             }
#         ],
#         "total_tax": 13.5,
#         "currency": "EUR"
#     }
# }
# order_data = json.loads(data)
# def create_order(api_url, access_token, order_data):
#     headers = {
#         'X-Shopify-Access-Token': access_token,
#         'Content-Type': 'application/json'
#     }
#     response = requests.post(api_url, json=order_data, headers=headers)
#     print(response.status_code,response.text)
#     if response.status_code == 201:
#         return response.json()
#     else:
#         return None

# Example usage:
# api_url = f'https://{shop_url}/admin/api/2024-07/orders.json'
# access_token = 'your_access_token'
 
   

# result = create_order(api_url, access_token, data)
# if result:
#     print("Order created successfully:", result)
# else:
#     print("Failed to create order.")

 