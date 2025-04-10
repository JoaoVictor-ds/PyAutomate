import pandas as pd
import os

# Caminho do arquivo XLSX (copie o seu arquivo como caminho e cole aqui)
caminho_xlsx = "C:\\Users\\renil\\Desktop\\Projetos\\Dataset.xlsx"

# Pasta de destino do CSV (Pasta onde você quer que seu CSV seja salvo)
pasta_destino = "C:\\Users\\renil\\Desktop\\Projetos"

# Nome do arquivo CSV (Nome que seu arquivo terá após a conversão para CSV)
nome_csv = "Dataset2.csv"

# Verifica se a pasta de destino existe, se não, ela é criada
if not os.path.exists(pasta_destino):
    os.makedirs(pasta_destino)

# Cria o caminho completo para o arquivo CSV de maneira simplificada e prática
caminho_csv = os.path.join(pasta_destino, nome_csv)

# Lê o arquivo XLSX
data = pd.read_excel(caminho_xlsx)

# Salva os dados em CSV no caminho (Passar "True" para índice caso queira que o pandas inclua a coluna "index")
data.to_csv(caminho_csv, index=False, encoding='utf-8')

print("Arquivo convertido com sucesso!")
