def main():
    # Lista para armazenar os números
    numeros = []

    # Solicitar ao usuário uma quantidade indefinida de números inteiros
    while len(numeros) < 4:
        try:
            num = int(input("Digite um número inteiro (pelo menos 4 valores são necessários): "))
            numeros.append(num)
        except ValueError:
            print("Entrada inválida. Por favor, digite um número inteiro.")

    # Continuar recebendo números até que o usuário decida parar
    while True:
        continuar = input("Deseja adicionar mais um número? (s/n): ").strip().lower()
        if continuar == 'n':
            break
        try:
            num = int(input("Digite outro número inteiro: "))
            numeros.append(num)
        except ValueError:
            print("Entrada inválida. Por favor, digite um número inteiro.")
    
    # Imprimir a lista original
    print("Lista original:", numeros)

    # Imprimir os 3 primeiros elementos
    print("Os 3 primeiros elementos:", numeros[:3])

    # Imprimir os 2 últimos elementos
    print("Os 2 últimos elementos:", numeros[-2:])

    # Imprimir a lista invertida
    print("Lista invertida:", numeros[::-1])

    # Imprimir os elementos de índice par
    print("Elementos de índice par:", numeros[::2])

    # Imprimir os elementos de índice ímpar
    print("Elementos de índice ímpar:", numeros[1::2])

if __name__ == "__main__":
    main()
