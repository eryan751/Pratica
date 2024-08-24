mf = str(input("Informe seu sexo [M/F]: ")).strip().upper()[0]

while mf not in "MmFf":
    mf = str(input("Dados invalidos, Informe seu sexo [M/F]: ")).strip().upper()[0]
    break

print("Ok")
