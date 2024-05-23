#Crie um sistema simples de cadastro e validação de usuários. Para isso, você vai gerenciar o arquivo 'usuarios.txt'. Seu sistema deve:
# - cadastrar novos usuários: verifica se o nome de usuário já existe no arquivo, em caso positivo, solicita um novo nome de usuário, em caso negativo, registra o nome em arquivo.
# - fazer login: solicita o nome de usuário, caso ele exista em arquivo, imprime "login efetuado com sucesso", caso contrário imprime "nome de usuário incorreto"

def carregar_usuarios():
    try:
        with open ('usuario.txt', 'r') as file:
            usuarios = file.read().splitlines()
        return usuarios
    except FileNotFoundError:
        return[]
    
def salvar_usuarios(usuario):
    with open ('usuario.txt', 'a') as file:
        file.write(usuario+'\n')

def cadastrar_usuario():
    usuarios = carregar_usuarios()
    while True:
        usuario = input('Digite um nome de usuário para cadastro: ')
        if usuario in usuarios:
            print("Nome de usuário já existe, por favor escolha outro nome: ")
        else:
            salvar_usuarios(usuario)
            print("Usuário cadastrado com sucesso!")
            break
def login():
    usuarios = carregar_usuarios()
    usuario = input("Digite seu nome de usuário: ")
    if usuario in usuarios:
        print ("Login efetuado com sucesso!")
    else:
        print("Nome de usuário incorreto.")

def main ():
    while True:
        print("\nEscolha uma opção:")
        print("1-Cadastrar novo usuário")
        print("2-Fazer login")
        print("3-Sair")
        opcao = int(input("Opção: "))

        if opcao == 1:
            cadastrar_usuario()
        elif opcao == 2:
            login()
        elif opcao == 3:
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()



