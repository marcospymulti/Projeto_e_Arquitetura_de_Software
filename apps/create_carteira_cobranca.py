import requests

url = "https://api-sandbox.kobana.com.br/v1/bank_billet_accounts"

payload = {
    "bank_contract_slug": "santander-bs-102",
    "agency_number": "0196",
    "account_number": "43331436",
    "account_digit": "5",
    "beneficiary_name": "Marcos",
    "beneficiary_cnpj_cpf": "75.764.487/0001-88",
    "beneficiary_address_street": "Rua Affonso Paula de Souza",
    "beneficiary_address_street_number": "2",
    "beneficiary_address_complement": "qd 6 lt 01",
    "beneficiary_address_neighborhood": "Conjunto Habitacional Ivo Tozzi",
    "beneficiary_address_city": "Araçatuba",
    "beneficiary_address_state": "SP",
    "beneficiary_address_zipcode": "16012615",
    "extra1": "12"
}
headers = {
    "Accept": "application/json",
    "Content-Type": "application/json",
    "Authorization": "Bearer 6RO7RQNliVsoz6YQ458Nqh2Rwg3SuXLFqYqR485aL1k"
}

response = requests.post(url, json=payload, headers=headers)

print(response.text)