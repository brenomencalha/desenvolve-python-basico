import sys, os

# Teste se o usuário passou o argumento
if len(sys.argv) == 1:
    print("Informe o nome do arquivo como argumento. Encerrando...")
    sys.exit()

# Teste se o argumento passado está correto
nome_arquivo = sys.argv[1]

if not os.path.isfile(nome_arquivo):
    print(f'Arquivo {nome_arquivo} não encontrado. Encerrando...')
    sys.exit()

# IMPORTANTE! Abrir o documento para escrita delete o arquivo, sem retorno.
#fp = open (nome_arquivo, 'w')

# Por padrão o arquivo é aberto para leitura, mas não custa ser redundante e especificar a leitura 'r':
fp = open (nome_arquivo, 'r')
fp_saida = open('invertido.txt', 'w')
for linha in fp:
    fp_saida.write(linha[::-1])
fp_saida.close()
fp.close()