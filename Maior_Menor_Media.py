def notas(*n, sit=False):
    r = dict()
    r["Quantidade de Notas"] = len(n)
    r["Maior Nota"] = max(n)
    r["Menor Nota"] = min(n)
    r["Média das Notas"] = sum(n)/len(n)
    if sit:
        if r["Média das Notas"] > 7:
            print("Boa Media")
        elif r["Média das Notas"]  > 5 and r["Média das Notas"] <7:
            print("Media OK")
        else:
            print("Media Baixa")
    return r


resp = notas(5.5, 3.9, 9, 6.3, sit=True)
print(resp)
