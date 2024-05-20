def validar_cpf(cpf):
    # Remover pontos e traço do CPF
    cpf = ''.join(filter(str.isdigit, cpf))

    # Verificar se o CPF tem 11 dígitos
    if len(cpf) != 11:
        return False

    # Calcular o primeiro dígito verificador
    soma = 0
    multiplicador = 10
    for i in range(9):
        soma += int(cpf[i]) * multiplicador
        multiplicador -= 1

    resto = soma % 11
    if resto < 2:
        digito_verificador_1 = 0
    else:
        digito_verificador_1 = 11 - resto

    # Verificar o primeiro dígito verificador
    if digito_verificador_1 != int(cpf[9]):
        return False

    # Calcular o segundo dígito verificador
    soma = 0
    multiplicador = 11
    for i in range(10):
        soma += int(cpf[i]) * multiplicador
        multiplicador -= 1

    resto = soma % 11
    if resto < 2:
        digito_verificador_2 = 0
    else:
        digito_verificador_2 = 11 - resto

    # Verificar o segundo dígito verificador
    if digito_verificador_2 != int(cpf[10]):
        return False

    # Se passou por todas as verificações, o CPF é válido
    return True

# Ler o CPF do usuário
cpf = input("Digite o CPF (XXX.XXX.XXX-XX): ")

# Validar o CPF
if validar_cpf(cpf):
    print ("CPF válido")
else:
    print("CPF inválido")
