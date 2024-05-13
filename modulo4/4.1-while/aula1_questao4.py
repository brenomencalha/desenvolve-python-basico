
n = int(input("Digite um valor qualquer para n: "))

maior = 0

while n > 0:
    x = int(input("Dê um valor para x: "))
    if x > maior:
        maior = x
        n = n - 1
    else:
        n = n - 1
print (f"O maior valor é {maior}.")

