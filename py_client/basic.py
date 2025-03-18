import requests
# import json

# endpoint = "https://httpbin.org/status/200/"
# endpoint = "https://httpbin.org/anything"
endpoint = "http://127.0.0.1:7000/api/"

get_response = requests.post(endpoint, json={"titles": "hello world", "content": "This is the content"})

# print(get_response.text)
# print(requests.get.text)
# body = requests.body
# data = {}
# try:
#     data = json.loads(body)
# except:
#     pass

# print(data)

# data['params'] = dict(request.GET)
# data['headers'] = dict(request.headers)
# data['content_type'] = request.content_type
#     return JsonResponse(data)

print(get_response.json())
# print(get_response.status_code)