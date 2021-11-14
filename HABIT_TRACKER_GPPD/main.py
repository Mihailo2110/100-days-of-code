import requests
from datetime import datetime
USERNAME = "mihailo"
TOKEN = "rdtrcftdrfyguh123"

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": "rdtrcftdrfyguh123",
    "username": "mihailo",
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

# graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/graph1/"

# graph_config = {
#     "id": "graph1",
#     "name": "Cycling graph",
#     "unit": "Km",
#     "type": "float",
#     "color": "ajisai"
# }

headers = {
    "X-USER-TOKEN": TOKEN
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

today = datetime(year=2021, month=10, day=5)
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/graph1/{today.strftime('%Y%m%d')}"
# graph_config = {
#     "quantity": "18",
# }
response = requests.delete(url=graph_endpoint, headers=headers)
print(response.text)