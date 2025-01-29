def ficha(jog='<desconhecido>', gols=0):
    """
    Exibe a ficha do jogador com nome e número de gols.
    
    Parâmetros:
    jog (str): Nome do jogador (opcional, padrão: '<desconhecido>')
    gols (int): Número de gols (opcional, padrão: 0)
    """
    print(f'O jogador {jog} fez {gols} gol(s) no campeonato.')

# Entrada de dados com tratamento de erros
nome = input("Nome: ").strip()

# Validação dos gols
while True:
    gols_input = input("Número de gols: ")
    try:
        gols = int(gols_input)
        break
    except ValueError:
        print("Erro! Digite um número inteiro para os gols.")

# Chamada da função
if not nome:  # Se o nome estiver vazio
    ficha(gols=gols)
else:
    ficha(nome, gols)