import csv

# Implementação do CRUD usuários #

# Os usuários serão armazenados no arquivo 'usuarios.csv' com os seguintes campos:

#id: identificador único do usuário;
# nome: nome de usuário;
# email: email do usuário;
# senha: senha do usuário;
# nível: nível de permissão do usuário (administrador, gerente, funcionário, cliente); 

def carregar_usuarios(caminho_arquivo):
    usuarios = []
    with open(caminho_arquivo, mode='r', newline='') as file:
        reader = csv.DictReader(file)
        for row in reader:
            usuarios.append(row)
    return usuarios

def salvar_usuarios(caminho_arquivo, usuarios):
    with open(caminho_arquivo, mode='w', newline='') as file:
        fieldnames = ['id', 'nome', 'email', 'senha', 'nivel']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        for usuario in usuarios:
            writer.writerow(usuario)
        
def criar_usuario(usuarios, id, nome, email, senha, nivel):
    novo_usuario = {'id': id, 'nome': nome, 'email': email, 'senha': senha, 'nivel': nivel}
    usuarios.append(novo_usuario)
    return usuarios

def ler_usuario(usuarios, id):
    for usuario in usuarios:
        if usuario['id'] == id:
            return usuario
    return None

def atualizar_usuario(usuarios, id, nome=None, email=None, senha=None, nivel=None):
    for usuario in usuarios:
        if usuario['id'] == id:
            if nome:
                usuario['nome'] = nome
            if email:
                usuario['email'] = email
            if senha:
                usuario['senha'] = senha
            if nivel:
                usuario['nivel'] = nivel
            return usuarios
    return None

def deletar_usuario (usuarios , id):
    for usuario in usuarios:
        if usuario['id'] == id:
            usuarios.remove(usuario)
            return usuarios
    return None

# Gerenciamento dos livros

# Estrutura de dados

# Os livros serão armazenados em um arquivo 'livros.csv' com os seguintes campos:

# código: código único do livro;
# título: título do livro;
# autor: nome do autor do livro;
# preço: preco do livro em R$;
# quantidade: quantidade em estoque;

def carregar_livros(caminho_arquivo):
    livros = []
    with open(caminho_arquivo, mode='r',newline='') as file:
        reader = csv.DictReader(file)
        for row in reader:
            livros.append(row)
    return livros

def salvar_livros(caminho_arquivo, livros):
    with open(caminho_arquivo, mode='w', newline='') as file:
        fieldnames = ['codigo', 'titulo', 'autor', 'preco', 'quantidade']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        for livro in livros:
            writer.writerow(livro)

def criar_livro(livros, codigo, titulo, autor , preco, quantidade):
    novo_livro = {'codigo': codigo, 'titulo': titulo, 'autor': autor, 'preco': preco, 'quantidade': quantidade}
    livros.append(novo_livro)
    return livros

def ler_livro(livros, codigo):
    for livro in livros:
        if livro['codigo'] == codigo:
            return livro
    return None

def atualizar_livro(livros, codigo, titulo=None, autor=None, preco=None, quantidade=None):
    for livro in livros:
        if livro['codigo'] == codigo:
            if titulo:
                livro['titulo'] = titulo
            if autor:
                livro['autor'] = autor
            if preco:
                livro['preco'] = preco
            if quantidade:
                livro['quantidade'] = quantidade
            return livros
    return None

def deletar_livro(livros, codigo):
    for livro in livros:
        if livro['codigo'] == codigo:
            livros.remove(livro)
            return livros
    return None

def buscar_livro(livros, termo):
    resultados = [livro for livro in livros if termo.lower() in livro['titulo'].lower() or termo.lower() in livro['autor'].lower()]
    return resultados

def ordenar_livros_por_nome(livros):
    return sorted(livros, key=lambda x: x['titulo'])

def ordenar_livros_por_preco(livros):
    return sorted(livros, key=lambda x: float(x['preco']))





    

