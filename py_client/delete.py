import requests

product_id = input("what is the product id you want to use ?")

try:
    product_id = int(product_id)
except:
    product_id = None
    print(f'{product_id} not a valid id')
    
if product_id:
    endpoint = "http://127.0.0.1:7000/api/products/2/{product_id}/delete/"
    get_response = requests.delete(endpoint)
    print(get_response.status_code, get_response.status_code==204)
