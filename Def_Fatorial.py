def fatorial(n, show=False):
    """
    -> Calcula o Fatorial de um número
    :param N: O Número a ser calculado.
    :param show: (opicional) Mostra a Conta ou Não.
    :return: Valor Fatorial de {n}
    Feito Pelo Guanabara
    """
    f = 1
    for c in range(n, 0, -1):
        if show:
            print(c, end=" ")
            if c > 1:
                print(f' x ', end="")
            else:
                print("=", end=" ")
        f *= c
    return f


help(fatorial)
#print(fatorial(5, show=True))
