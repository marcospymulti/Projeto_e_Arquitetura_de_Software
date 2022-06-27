import requests
from datetime import *

# Consulmo da API do boleto
url = "https://api-sandbox.kobana.com.br/v1/bank_billets?bank_billet_account_id=4669&status=opened&cnpj_cpf=75.764.487%2F0001-88&per_page=50"

headers = {
    "Accept": "application/json",
    "Authorization": "Bearer 6RO7RQNliVsoz6YQ458Nqh2Rwg3SuXLFqYqR485aL1k"
}

response = requests.get(url, headers=headers)

#print(response.text)

# funcionalidade para notificação do vencimento do boleto 
resposta_boleto = response.json()

#print(resposta_boleto[0]["expire_at"])
data_vencimento_boleto = resposta_boleto[0]["expire_at"] #'2022-06-24'
#print(data_vencimento_boleto)

# data do sistema/ do dia atual
data_atual = date.today()
data_atual = str(data_atual)
#print(data_atual)


# Data final
d2 = datetime.strptime(data_vencimento_boleto, '%Y-%m-%d')

# Data inicial
d1 = datetime.strptime(data_atual, '%Y-%m-%d')

# 
#quantidade_dias_para_vencimento = abs((d2 - d1).days)
quantidade_dias_para_vencimento = (d2 - d1).days
#print(quantidade_dias_para_vencimento)

# Tranformando string datas em objetos date
data_vencimento_boleto = datetime.strptime(data_vencimento_boleto, '%Y-%m-%d').date()

#Personalizando alertas de acordo com dias faltantes
if quantidade_dias_para_vencimento == 10:
    print(f'Seu boleto vence daqui {quantidade_dias_para_vencimento} dias, na data: {data_vencimento_boleto.strftime("%d/%m/%Y")}. Se já realizou o pagamento, desconsidere a mensagem.')
elif quantidade_dias_para_vencimento == 5:
    print(f'Seu boleto vence daqui {quantidade_dias_para_vencimento} dias, na data: {data_vencimento_boleto.strftime("%d/%m/%Y")}. Se já realizou o pagamento, desconsidere a mensagem.')
elif quantidade_dias_para_vencimento == 0:
    print(f'Seu boleto vence Hoje: {data_vencimento_boleto.strftime("%d/%m/%Y")}. Se já realizou o pagamento, desconsidere a mensagem.')
#boleto ja vencido
elif quantidade_dias_para_vencimento < 0:
    print(f'Seu boleto venceu na data : {data_vencimento_boleto.strftime("%d/%m/%Y")}, realize o pagamento. Se já realizou o pagamento, desconsidere a mensagem.')




