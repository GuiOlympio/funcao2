from time import sleep 

# Lista de códigos de cores ANSI para formatação do terminal
c = ('\33[m',        # 0 - Sem cor (reset)
    '\33[0;30;41m', # 1 - Vermelho com fundo vermelho e texto preto
    '\33[0;30;42m', # 2 - Verde com fundo verde e texto preto
    '\33[0;30;43m', # 3 - Amarelo com fundo amarelo e texto preto
    '\33[0;30;44m', # 4 - Azul com fundo azul e texto preto
    '\33[0;30;45m', # 5 - Roxo com fundo roxo e texto preto
    '\33[7;30m',    # 6 - Invertido (texto preto com fundo branco)
)

def ajuda(com):
    """
    Exibe o manual de ajuda para um comando específico.
    
    Parâmetros:
        com (str): Comando ou biblioteca para consultar a ajuda
    """
    titulo(f'Acessando manual do comando \'{com}\'', 5)  # Título em roxo
    print(c[6], end='')  # Muda para cor invertida (branco)
    help(com)  # Mostra a ajuda do comando
    print(c[2], end='')  # Volta para cor verde
    sleep(2)  # Pausa para leitura

def titulo(msg, cor=0):
    """
    Cria um título formatado com bordas coloridas.
    
    Parâmetros:
        msg (str): Texto do título
        cor (int): Índice da cor na lista 'c' (0-6)
    """
    tam = len(msg) + 4  # Calcula tamanho das bordas
    print(c[cor], end='')  # Aplica a cor selecionada
    print('=+' * tam)  # Borda superior
    print(f'   {msg}')  # Mensagem centralizada
    print('=+' * tam)  # Borda inferior
    print(c[0], end='')  # Reseta a cor
    sleep(1)  # Pausa para efeito visual

# Loop principal do programa
comando = ''
while True:
    titulo("SISTEMA DE AJUDA PyHelp", 2)  # Título principal em verde
    comando = str(input("Função ou Biblioteca -> ")).strip().lower()
    
    if comando.upper() == 'FIM':
        break  # Sai do loop se digitar 'FIM'
    else:
        ajuda(comando)  # Mostra ajuda do comando

titulo("Até logo!", 1)  # Mensagem de despedida em vermelho