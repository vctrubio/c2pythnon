import requests

person_data = {
    "name": "John Doe",
    "tickets": 2
}


# Create
response = requests.post("http://127.0.0.1:8000/persons/", json=person_data)
print(response.status_code)
print(response.text)

'''
import requests

person_data = {
    "name": "John Doe",
    "tickets": [{"ticket_data_key": "value"}]
}

# Create
response = requests.post("http://127.0.0.1:8000/persons/", json=person_data)
print(response.status_code)
print(response.text)
'''