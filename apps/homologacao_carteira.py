import requests

url = "https://api-sandbox.kobana.com.br/v1/bank_billet_accounts/4669/ask"

headers = {
    "Accept": "application/json",
    "Authorization": "Bearer 6RO7RQNliVsoz6YQ458Nqh2Rwg3SuXLFqYqR485aL1k"
}

response = requests.get(url, headers=headers)

print(response.text)