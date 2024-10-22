soma = 0
cont = 0
for c in range(1, 7):
    n = int(input(f"Digite o {c} valor: "))
    cont+=1
    soma+=n
    
print(f"Você informou {cont} números e a soma foi {soma}")
