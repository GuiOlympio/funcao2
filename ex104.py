def leiaInt(msg):
    """
    Função que lê um número inteiro válido do usuário.
    
    Parâmetros:
    msg (str): Mensagem de prompt para a entrada do usuário.
    
    Retorna:
    int: Número inteiro validado.
    """
    while True:
        try:
            valor = int(input(msg))
            return valor
        except ValueError:
            print('\033[31mERRO! Digite um número inteiro válido.\033[m')

# Teste da função
n = leiaInt("Digite um número: ")
print(f'Você digitou o número {n}')