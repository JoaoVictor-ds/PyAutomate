import requests
import pandas as pd
import matplotlib.pyplot as plt

# coletando cotações 
url = r"https://economia.awesomeapi.com.br/json/last/USD-BRL,EUR-BRL,BTC-BRL"

# requesição get
response = requests.get(url)

# vericando se a requisição foi bem sucedida
if response.status_code == 200:
    dados = response.json()

    # extraindo valores 
    usd_brl = dados.get("USDBRL", {}).get("bid")
    eur_brl = dados.get("EURBRL", {}).get("bid")
    btc_brl = dados.get("BTCBRL", {}).get("bid")

    # salvas os reultados como um pandas dataframe
    df = pd.DataFrame({
    "Moeda": ["USD-BRL", "EUR-BRL", "BTC-BRL"],
    "Valor": [usd_brl, eur_brl, btc_brl]
    })
    
    # salvar os resultados em csv
    try:
        salvar_csv = df.to_csv(r"C:\Users\renil\Desktop\Projeto_cotacao.csv" , index= False)
        print("csv criado com sucesso")
    except Exception as e:
        print(f"Erro na criação do arquivo csv: {e}")

    # valores para usar no gráfico
    moedas = ["USD-BRL", "EUR-BRL", "BTC-BRL"]  
    valores = [usd_brl, eur_brl, btc_brl]

    # configurando o gráfico
    plt.plot(moedas, valores, color= 'skyblue', marker= 'o', linestyle='-', label='Cotações')
    plt.title("Cotações em Reais")
    plt.xlabel("Moedas")
    plt.ylabel("Valor")
    plt.tight_layout()

    # cria um gráfico e o armazena na pasta especificada
    plt.savefig(r"C:\Users\renil\Desktop\Projeto_cotacao\cotação_atual.png", dpi= 300, bbox_inches= "tight")
    plt.show()

    # exibe o resultado no terminal
    print(f"Dólar (USD -> BRL): R$ {usd_brl}")
    print(f"Euro (EUR -> BRL): R$ {eur_brl}")
    print(f"Bitcoin (BTC -> BRL): R$ {btc_brl}")

# em caso de erro
else:
    print(f"Erro ao acessar a API: {response.status_code}")
              