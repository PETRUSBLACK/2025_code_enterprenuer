import requests

endpoint = "http://127.0.0.1:7000/api/products/2/update"

data = {
    "title": "Hello world my old friend",
    "price": 129.99
}

get_response = requests.put(endpoint, json=data)


print(get_response.json())
