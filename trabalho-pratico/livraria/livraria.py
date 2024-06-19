import utils

def menu_principal():
    print("--- Livraria Online ---")
    print("1. Gerenciar usuários")
    print("2. Gerenciar livros")
    print("3. Sair")

    escolha = input("Escolha uma opção:")
    return escolha

def menu_usuarios():
    print("--- Gerenciamento de usuários ---")
    print("1. Criar usuário")
    print("2. Ler usuário")
    print("3. Atualizar usuário")
    print("4. Deletar usuário")
    print("5. Voltar")

    escolha = input("Escolha uma opção:")
    return escolha

def menu_livros():
    print("--- Gerenciamento de livros ---")
    print("1. Criar livro")
    print("2. Ler livro")
    print("3. Atualizar livro")
    print("4. Deletar livro")
    print("5. Buscar livro")
    print("6. Ordenar livros por nome")
    print("7. Ordenar livros por preço")
    print("8. Voltar")

    escolha = input("Escolha uma opção:")
    return escolha

def main():
    usuarios = utils.carregar_usuarios('data/usuarios.csv')
    livros = utils.carregar_livros('data/livros.csv')

    while True:
        escolha = menu_principal()

        if escolha == '1':
            while True:
                escolha_usuario = menu_usuarios()

                if escolha_usuario == '1':
                    id = input("ID: ")
                    nome = input("Nome: ")
                    email = input("Email: ")
                    senha = input("Senha: ")
                    nivel = input("Nível (administrador, gerente, funcionário, cliente): ")
                    usuarios = utils.criar_usuario(usuarios, id, nome, email, senha, nivel)
                    utils.salvar_usuarios('data/usuarios.csv', usuarios)
                
                elif escolha_usuario == '2':
                    id = input("ID: ")
                    usuario = utils.ler_usuario(usuarios, id)
                    print(usuario)
                
                elif escolha_usuario == '3':
                    id = input("ID: ")
                    nome = input("Novo Nome (ou enter para manter): ")
                    email = input("Novo Email(ou enter para manter): ")
                    senha = input("Nova Senha (ou enter para manter): ")
                    nivel = input("Novo Nível (ou enter para manter): ")
                    usuarios = utils.atualizar_usuario(usuarios, id, nome, email, senha, nivel)
                    utils.salvar_usuarios('data/usuarios.csv', usuarios)
                
                elif escolha_usuario == '4':
                    id = input("ID: ")
                    usuarios = utils.deletar_usuario(usuarios, id)
                    utils.salvar_usuarios('data/usuarios.csv', usuarios)
                
                elif escolha_usuario == '5':
                    break

        elif escolha == '2':
            while True:
                escolha_livro = menu_livros()

                if escolha_livro == '1':
                    codigo = input("Código: ")
                    titulo = input("Título: ")
                    autor = input("Autor: ")
                    preco = input("Preço: ")
                    quantidade = input("Quantidade: ")
                    livros = utils.criar_livro(livros, codigo, titulo, autor, preco, quantidade)
                    utils.salvar_livros('data/livros.csv', livros)

                elif escolha_livro == '2':
                    codigo = input("Código: ")
                    livro = utils.ler_livro(livros, codigo)
                    if livro:
                        print(livro)
                    else:
                        print("Livro não encontrado.")

                elif escolha_livro == '3':
                    codigo = input("Código: ")
                    titulo = input("Novo Título (ou enter para manter): ")
                    autor = input("Novo Autor (ou enter para manter): ")
                    preco = input("Novo Preço (ou enter para manter): ")
                    quantidade = input("Nova Quantidade (ou enter para manter): ")
                    livros = utils.atualizar_livro(livros, codigo, titulo, autor, preco, quantidade)
                    utils.salvar_livros('data/livros.csv', livros)
                
                elif escolha_livro == '4':
                    codigo = input("Código: ")
                    livros = utils.deletar_livro(livros, codigo)
                    utils.salvar_livros('data/livros.csv', livros)

                elif escolha_livro == '5':
                    termo = input("Termo de busca (título ou autor): ")
                    resultados = utils.buscar_livro(livros, termo)
                    for livro in resultados:
                        print (livro)
                
                elif escolha_livro == '6':
                    livros_ordenados = utils.ordenar_livros_por_nome(livros)
                    for livro in livros_ordenados:
                        print(livro)

                elif escolha_livro == '7':
                    livros_ordenados = utils.ordenar_livros_por_preco(livros)
                    for livro in livros_ordenados:
                        print (livro)
                
                elif escolha_livro == '8':
                    break
        
        elif escolha == '3':
            break

if __name__ == "__main__":
    main()

                    



