import requests

# Replace these variables with your actual values
# shopify_store = 'your-shop'
password = ''
shop = 'quickstart-b4fa8ebd'
access_token = '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'
# cli_token = 'atkn_20eaf778ff3ea2aae723595588b7078080228d474e0183414d58600007900682'
import requests

url = "https://{shop}.myshopify.com/admin/api/2024-01/products.json"
headers = {
    "Content-Type": "application/json",
    # "X-Shopify-Access-Token": "{access_token}"
}

response = requests.get(url, headers=headers)

# if response.status_code == 200:
#     data = response.json()
#     # print(data)
# else:
#     print("Error:", )
#     # print(response.text)
