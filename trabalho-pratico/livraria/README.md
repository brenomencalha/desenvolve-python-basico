# Livraria Online

## Visão Geral

Este projeto é um sistema de gerenciamento para uma livraria online. Ele permite que você gerencie usuários e livros utilizando operações CRUD (Criar, Ler, Atualizar, Deletar). O sistema armazena dados de usuários e livros em arquivos CSV e inclui um menu interativo para facilitar a navegação.

## Funcionalidades

### Usuários

- **Criar Usuário**: Adiciona um novo usuário ao sistema.
- **Ler Usuário**: Recupera e exibe informações de um usuário existente.
- **Atualizar Usuário**: Atualiza as informações de um usuário existente.
- **Deletar Usuário**: Remove um usuário do sistema.
- **Voltar**: Retorna ao menu principal.

### Livros

- **Criar Livro**: Adiciona um novo livro ao sistema.
- **Ler Livro**: Recupera e exibe informações de um livro existente.
- **Atualizar Livro**: Atualiza as informações de um livro existente.
- **Deletar Livro**: Remove um livro do sistema.
- **Buscar Livro**: Busca livros pelo título ou autor.
- **Ordenar Livros por Nome**: Exibe todos os livros ordenados por nome.
- **Ordenar Livros por Preço**: Exibe todos os livros ordenados por preço.
- **Voltar**: Retorna ao menu principal.

## Estrutura do Projeto

O projeto é composto pelos seguintes arquivos:

- `livraria.py`: Arquivo principal do sistema, contendo a lógica do menu e as funcionalidades principais.
- `utils.py`: Contém funções auxiliares para carregar, salvar e manipular dados de usuários e livros.
- `data/usuarios.csv`: Arquivo de dados onde os usuários são armazenados.
- `data/livros.csv`: Arquivo de dados onde os livros são armazenados.

## Como Executar

1. **Pré-requisitos**: Certifique-se de ter o Python 3 instalado em seu sistema.

2. **Clonar o Repositório**:
    ```sh
    git clone https://github.com/seuusuario/livraria-online.git
    cd livraria-online
    ```

3. **Executar o Script**:
    ```sh
    python livraria.py
    ```

## Estrutura dos Arquivos de Dados

### usuarios.csv

O arquivo `usuarios.csv` armazena os dados dos usuários no seguinte formato:

id,nome,email,senha,nivel
1,João Silva,joao@example.com,senha123,gerente
2,Maria Oliveira,maria@example.com,senha456,funcionario


### livros.csv

O arquivo `livros.csv` armazena os dados dos livros no seguinte formato:

codigo,titulo,autor,preco,quantidade
1,O Senhor dos Anéis,J.R.R. Tolkien,39.90,10
2,1984,George Orwell,29.90,5


## Como Utilizar

1. **Menu Principal**:
    - Escolha entre gerenciar usuários ou livros, ou sair do sistema.

2. **Gerenciamento de Usuários**:
    - Selecione a operação desejada (Criar, Ler, Atualizar, Deletar) e siga as instruções para inserir os dados necessários.

3. **Gerenciamento de Livros**:
    - Selecione a operação desejada (Criar, Ler, Atualizar, Deletar, Buscar, Ordenar) e siga as instruções para inserir os dados necessários.

## Contribuindo

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues e enviar pull requests para melhorias no projeto.

## Instruções Adicionais:

Criação dos Arquivos CSV:
Se os arquivos usuarios.csv e livros.csv não existirem, crie-os manualmente com os cabeçalhos apropriados conforme mencionado na seção "Estrutura dos Arquivos de Dados".

## Dependências:

Atualmente, este projeto não tem dependências adicionais além do Python 3.
