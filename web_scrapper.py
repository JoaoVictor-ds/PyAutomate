import requests 
from bs4 import BeautifulSoup
import re 
import os

# link da página

pagina = requests.get(r"https://quotes.toscrape.com/")

# verificando se é possivel acessar a página e obtendo dados da página

if pagina.status_code == 200:
    dados_pagina = BeautifulSoup(pagina.text , 'html.parser')

# em caso de erro de requisição
else:
    print(f"erro ao requisitar url do site {pagina.status_code}")

# obter todas as frases 

frases = dados_pagina.find_all('div' , class_= "quote")

# variável onde ficaram armazeanadas as frases já filtradas

frases_filtradas = []

# filtrar apenas frases que contenham uma palavra especifica 
# nesse caso para exemplo estou usando a palavra "world"

for div in frases:
    texto = div.find('span' , class_= "text").text
    if re.search(r'\bworld\b', texto, re.IGNORECASE):
        frases_filtradas.append(texto)

        # imprimir o resultado no terminal

        print(texto)

# salvando resultados em um arquivo CSV

with open("frases_filtradas.txt", "w", encoding="utf-8") as arquivo_txt:
        arquivo_txt.writelines(frases_filtradas)


# verificando possiveis erros
if os.path.exists("resultados_scrap"): 
        print("resultados salvos em txt com sucesso")

else:
        print("Erro ao salvar resultados em arquivo CSV")

