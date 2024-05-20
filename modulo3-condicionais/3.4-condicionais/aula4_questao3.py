# Ano bissexto - Condições
# 1 - ano divisível por 4 e não for divisível por 100 ou
# 2 - ano divisível por 400.

contador = 0
while contador < 4:
    ano = int(input("Digite um ano qualquer: "))

    if (ano % 4 == 0) and (ano % 100 != 0) or (ano % 400 == 0):
        print (f" O ano {ano} é Bissexto!")
    else:
        print (f"O ano {ano} não é Bissexto!")
    contador = contador + 1

