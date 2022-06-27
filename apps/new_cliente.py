import requests
from datetime import *
# url = "https://api-sandbox.kobana.com.br/v1/customers"

# payload = {
#     "person_name": "Marcos",
#     "nickname": "marcos",
#     "address": "Rua Affonso Paula de Souza",
#     "state": "sp",
#     "city_name": "Araçatuba",
#     "neighborhood": "Conjunto Habitacional Ivo Tozzi",
#     "zipcode": "16012615",
#     "cnpj_cpf": "75.764.487/0001-88"
# }
# headers = {
#     "Accept": "application/json",
#     "Content-Type": "application/json",
#     "Authorization": "Bearer 6RO7RQNliVsoz6YQ458Nqh2Rwg3SuXLFqYqR485aL1k"
# }

# response = requests.post(url, json=payload, headers=headers)

# print(response.text)

# Consulta de cliente
url = "https://api-sandbox.kobana.com.br/v1/customers"

headers = {
    "Accept": "application/json",
    "Authorization": "Bearer 6RO7RQNliVsoz6YQ458Nqh2Rwg3SuXLFqYqR485aL1k"
}

response = requests.get(url, headers=headers)

print(response.text)
