def formatar_numero(numero):
    # Remover espaços em branco e caracteres não numéricos
    numero = ''.join(c for c in numero if c.isdigit())

    # Verificar o comprimento do número
    if len(numero) == 8:
        numero = '9' + numero  # Acrescentar '9' na frente do número
        numero = numero[:5] + '-' + numero[5:]  # Adicionar "-" após o quinto dígito
    elif len(numero) == 9:
        numero = numero[:5] + '-' + numero[5:]  # Adicionar "-" após o quinto dígito

    return numero

# Ler o número de celular do usuário
numero_celular = input("Digite o número de celular: ")

# Formatar o número de celular
numero_formatado = formatar_numero(numero_celular)

# Imprimir o número de celular formatado
print("Número de celular formatado:", numero_formatado)
