def fatorial(n=1, show=False):
    """
    Calcula o fatorial de um número.
    
    :param n: Número a ser calculado.
    :param show: (Opcional) Mostra o processo de cálculo quando True.
    :return: Valor do fatorial de n.
    """
    f = 1
    for i in range(n, 0, -1):
        f *= i
        if show:
            print(i, end='')
            if i > 1:
                print(" x ", end="")
            else:
                print(f" = {f}", end="")
    if show:
        print()  # Pula linha após o cálculo
    return f

# Teste
print(fatorial(5, show=True))
help(fatorial)