#Aposentadoria - Regras

#A: Para mulheres, ter mais de 60 anos. Para homens, 65.
#B: Ou ter trabalhado pelo menos 30 anos
#C: Ou ter 60 anos  e trabalhado pelo menos 25.

#entrada
genero_usuario = input ("Qual o seu gênero? (M ou F): ")
idade = int(input ("Qual sua idade? "))
anos_servico = int(input("Forneça seu tempo de serviço em anos: "))

#processamento/saída

if (genero_usuario == "F" or genero_usuario == "f") and (idade > 60) or (anos_servico >= 30) or (anos_servico >= 25 and idade >= 60):
    print (True)

elif (genero_usuario == "M" or genero_usuario == "m") and (idade > 65) or (anos_servico >= 30) or (anos_servico >= 25 and idade >= 60):
    print (True)
    
else:
    print (False)
