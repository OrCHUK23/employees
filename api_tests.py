import requests, json


# Check GET request.
def get_request(url):
    response = requests.get(url=url)
    if response.raise_for_status(): # If there's a problem.
        return False
    else:
        return response.json()
    

# Check POST request.
def post_request(url):
    simple_json = {"name": "Moshe"}
    response = requests.post(url=url, json=simple_json)
    if response.raise_for_status(): # If there's a problem.
        print (response.text)
        return False
    else:
        return response.json()["id"]
    

# # Check PUT request.
# def put_request(id):
#     simple_json = {"name": "Moshiko"}
#     response = requests.put(url='http://127.0.0.1:5000/employees/f{id}', json=simple_json)
#     if response.raise_for_status(): # If there's a problem.
#         return False
#     else:
#         return response.json()
    

url = 'http://localhost:5000/employees'
# print("Get request result: \n", get_request(url=url))
print("Post request reuslt:\n", post_request(url=url))