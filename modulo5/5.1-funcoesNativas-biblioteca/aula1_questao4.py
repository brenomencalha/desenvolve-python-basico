#Escreva um programa em Python que utiliza a biblioteca datetime para exibir a data e hora atuais

from datetime import datetime

data_e_hora_atual = datetime.now ()
data_e_hora = data_e_hora_atual.strftime('%d/%m/%Y %H:%M')

print(data_e_hora)