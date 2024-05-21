def converter_data(data):
    # Lista dos meses por extenso
    meses = [
        "Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho",
        "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"
    ]

    # Divide a data em dia, mês e ano
    dia, mes, ano = data.split('/')

    # Converte o mês de número para nome
    mes_extenso = meses[int(mes) - 1]

    # Retorna a data no formato desejado
    return f"Você nasceu em {dia} de {mes_extenso} de {ano}."

# Solicita a data de nascimento do usuário
data_nascimento = input("Digite uma data de nascimento (dd/mm/aaaa): ")

# Converte e imprime a data no formato desejado
data_formatada = converter_data(data_nascimento)
print(data_formatada)
