import requests

url = "https://jsonplaceholder.typicode.com/users"
api_key = "your_api_key_here"  # Replace with your actual API key if needed
headers = {
    "Authorization": f"Bearer {api_key}"
}
r = requests.get(url, headers=headers, timeout=10)
status = r.status_code
print(f"Status Code: {status}")
users = r.json()
for user in users:
    print(f"User: {user['name']}, Email: {user['email']}")

# POST request example
user = {
    "name": "John Doe",
}
create_request = requests.post(url, timeout=10, data=user)
print(f"Create Status Code: {create_request.status_code}")


# PUT request example
update_user = {
    "name": "Jane Doe",
}
update_request = requests.put(f"{url}/1", timeout=10, data=update_user)
print(f"Update Status Code: {update_request.status_code}")