import requests
import json

#pergunta para o usuario
p1 = float (input ('digite um valor em R$ para converter em dolar: '))

#variavel para armazena a API
api = 'https://economia.awesomeapi.com.br/json/last/USD-BRL'

#extração da cotaçao em dolar em json
api123 = requests.get(api)
cotacoes = api123.json()
valor_dolar = cotacoes['USDBRL'] ['bid'] #extraçao do valor do dolar

#conversão do dolar em json para um valor flutuante (float)
real_dolar = float (valor_dolar)

#soma da converção de dolar para real
soma = (p1 / real_dolar)

#exibição para da converçao para o usuario
print (f'com {p1}R$ você consegue converter para {soma} dolar.')