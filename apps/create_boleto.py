import requests

# Criar boleto via post
url = "https://api-sandbox.kobana.com.br/v1/bank_billets"

payload = {
    "interest_type": 0,
    "interest_days_type": 0,
    "fine_type": 0,
    "discount_type": 0,
    "charge_type": 1,
    "dispatch_type": 1,
    "document_type": "02",
    "acceptance": "N",
    "bank_billet_account_id": 4669,
    "bank_billet_layout_id": 1,
    "amount": 10000000,
    "expire_at": "2022-07-12",
    "customer_id": 176427,
    "customer_person_name": "Marcos",
    "customer_cnpj_cpf": "75.764.487/0001-88",
    "customer_state": "SP",
    "customer_city_name": "Araçatuba",
    "customer_zipcode": "16012615",
    "customer_address": "Rua Affonso Paula de Souza",
    "customer_neighborhood": "Conjunto Habitacional Ivo Tozzi"
}
headers = {
    "Accept": "application/json",
    "Content-Type": "application/json",
    "Authorization": "Bearer 6RO7RQNliVsoz6YQ458Nqh2Rwg3SuXLFqYqR485aL1k"
}

response = requests.post(url, json=payload, headers=headers)

print(response.text)