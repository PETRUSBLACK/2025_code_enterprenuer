import requests

endpoint = "http://127.0.0.1:7000/api/products/"

data = {
    "title": "This field is done",
    "price": 13.39
}

get_response = requests.post(endpoint, json=data)


print(get_response.json())
