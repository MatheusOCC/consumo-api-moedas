import requests #Requisição a Base Web
import json     #Entende o dicionário Json da Web
import pandas   #Exporta Excel

url = "http://data.fixer.io/api/latest?access_key=3248a6b9ae77624138f5c6e3cd3dad9d"
print("Acessando Base de Dados...")
resposta = requests.get(url)
print(resposta)
if resposta.status_code == 200:
    print("Acesso bem-sucedido!")
    print("Buscando informações...")
    dados = resposta.json()

    dolar_real = dados['rates']['BRL']/dados['rates']['USD']
    euro_real = dados['rates']['BRL']/dados['rates']['EUR']
    bitcoin_real = dados['rates']['BRL']/dados['rates']['BTC']

    print("R$",round(dolar_real, 2))
    print("R$",round(euro_real, 2))
    print("R$",round(bitcoin_real, 2))

    print("exportando resultado em tabela excel...")
    tela = pandas.DataFrame({'Moedas':['Dolar', 'Euro', 'Bitcoin'],
                            'Valores':[dolar_real, euro_real, bitcoin_real]})
    tela.to_csv('valores.csv', index=False, sep=";", decimal=",")
    print("Arquivo gerado com Sucesso!")

else:
    print("Erro na Base de Dados!")