# Projeto_e_Arquitetura_de_Software

## Execução do projeto

Linguagem usada: Python 3.9.8 

1º Clonar repositório: git clone https://github.com/marcospymulti/Projeto_e_Arquitetura_de_Software.git

2º Criar ambiente virtual (usar gerênciador da sua preferência): virtualenv env

3º Ativar ambiente virtual: env\Scripts\activate

4º Instalação de bibliotecas e pacotes: pip install -r requeriments.txt


Descrição do projeto:

Cosumo de API para integração com módulo financeiro. Foi realizado a criação do cliente, criação da carteira de cobrança, homologação da carteira de cobrança, criação do boleto, consulta do boleto.

Serviço criado apartir do consumo da API: Serviço de notificação de vencimento do boleto. A notificação alerta o usuário proximo ao vencimento e no dia do vencimento. Após vencido, a notificação é diária.