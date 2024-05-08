import requests

# Fazendo a requesição com a biblioteca requests
url = "https://cdn.moeda.info/api/latest.json"
resposta = requests.get(url)
dados = resposta.json()["rates"]

stop = 0
while stop != "2":
    stop = 0
    # Mostrando as opções disponíveis para conversão com base no dicionário de valores que retornou
    print("-------------------------------------------------------------")
    print("Moedas disponíveis:\n ")
    print("USD - Dólar Americano") 
    print("EUR - Euro")
    print("BRL - Real Brasileiro")
    print("GBP - Libra Esterlina")
    print("ARS - Peso Argentino")
    print("AUD - Dólar Australiano")
    print("JPY - Yen")
    print("BTC - Bitcoin")
    print("CZK - Coroa Checa")
    print("THB - Baht Tailandês")
    print("-------------------------------------------------------------")
    moeda_para_conversao = input("Digite qual moeda deseja converter? ").upper()
    moeda_para_conversao = ''.join(moeda_para_conversao.split())
    print("-------------------------------------------------------------")

    while True:
        try:
            valor_moeda = float(input("Qual o valor em {} que você deseja converter? ".format(moeda_para_conversao)))
            break
        except ValueError:
            print("Por favor, insira um número válido.")
    print("-------------------------------------------------------------")

    moeda_convertida = input("Para qual moeda deseja converter? ").upper()
    moeda_convertida = ''.join(moeda_convertida.split())
    print("-------------------------------------------------------------")

    moedas = [moeda_para_conversao , moeda_convertida]

    if moeda_para_conversao and moeda_convertida in ["USD","EUR","BRL","GBP","ARS","AUD","JPY","BTC","CZK","THB"]:

        # Convertendo as moedas para float
       
        moeda_para_conversao = float(dados[moeda_para_conversao])
        moeda_convertida = float(dados[moeda_convertida])
       
        # Calculando a taxa de câmbio e realizando a conversão

        taxa_de_cambio = moeda_convertida / moeda_para_conversao
    
        if moeda_para_conversao < moeda_convertida:
            taxa_de_cambio_1 = moeda_para_conversao / moeda_convertida
            conversao = valor_moeda / taxa_de_cambio_1

        else:
            conversao = valor_moeda * taxa_de_cambio
    
        print("Valor convertido: {:.2f} {} - Para cada 1 {} são {:.2f} {}".format(conversao,moedas[1],moedas[0],taxa_de_cambio,moedas[1]))
        print("-------------------------------------------------------------")
    else:
        print("Oops alguma moeda que você escolheu não está na lista.")
        print("-------------------------------------------------------------")
    while stop != ("1" or "2"):
        stop = (input("Digite [1] para converter novamente ou [2] para sair: "))
        if stop in ["1","2"]:
            break
        else:
            print("Valor inválido")
            