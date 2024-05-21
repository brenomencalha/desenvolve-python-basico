import re

def validador_senha(senha):
    # Verifica se a senha tem pelo menos 8 caracteres
    if len(senha) < 8:
        return False
    
    # Verifica se a senha contém pelo menos uma letra maiúscula
    if not re.search(r'[A-Z]', senha):
        return False
    
    # Verifica se a senha contém pelo menos uma letra minúscula
    if not re.search(r'[a-z]', senha):
        return False
    
    # Verifica se a senha contém pelo menos um número
    if not re.search(r'\d', senha):
        return False
    
    # Verifica se a senha contém pelo menos um caractere especial
    if not re.search(r'[@#$%^&+=]', senha):
        return False
    
    # Se todas as condições forem atendidas, a senha é válida
    return True

# Testando a função
senhas = [
    "Senha123@",
    "senhafraca",
    "Senha_fraca"        
]

for senha in senhas:
    if validador_senha(senha):
        print(f'"{senha}" é uma senha válida.')
    else:
        print(f'"{senha}" não é uma senha válida.')
