import openpyxl
from urllib.parse import quote
import webbrowser
from time import sleep
import pyautogui
import os 
from datetime import datetime

# abre o whatsapp no navegador 
webbrowser.open('https://web.whatsapp.com/')

# salva a planilha excel 
planilha = openpyxl.load_workbook("Clientes_3.xlsx")
planilha_clientes = planilha['Planilha1']

# percorre a planilha
for linha in planilha_clientes.iter_rows(min_row=2):

    # salva as informações do cliente desejado
    nome = linha[0].value
    vencimento_fatura = linha[1].value
    telefone_celular = linha[2].value 

    # validação de dados 
    if not nome or not telefone_celular or not vencimento_fatura: 
          print(f"dados incompletos em {linha[0].value}")
          continue 

    # muda a saudação a depender do horário 
    hora_atual = datetime.now().hour
    if hora_atual < 12:
          saudacao = "Bom dia"
    if 12 <= hora_atual < 18:
          saudacao = "Boa tarde"
    if hora_atual > 18:
          saudacao = "Boa noite"   


# mensagem a ser enviada para o cliente
mensagem = f"{saudacao} {nome}, seu fatura vence dia {vencimento_fatura}, pague aqui https://pagamento.com"


# Envia a mensagem, caso não seja possível armazena o erro em um CSV
try:
    link_whatsapp = f"https://web.whatsapp.com/send?phone={telefone_celular}&text={quote(mensagem)}"
    webbrowser.open(link_whatsapp)
    sleep(10)
    seta = pyautogui.locateCenterOnScreen('seta.png')
    sleep(2)
    pyautogui.click(seta[0],seta[1])
    sleep(2)
    pyautogui.hotkey('ctrl','w')
    sleep(2)
except:
        print(f'Não foi possível enviar mensagem para {nome}')
        with open('erros.csv','a',newline='',encoding='utf-8') as arquivo:
                 arquivo.write(f'{nome},{telefone_celular}{os.linesep}')

