from datetime import datetime

def voto(ano_nascimento):
    """
    Função que determina a obrigatoriedade do voto com base no ano de nascimento.
    
    Parâmetros:
    ano_nascimento (int): Ano de nascimento da pessoa
    
    Retorna:
    str: Situação eleitoral formatada
    """
    idade = datetime.now().year - ano_nascimento
    
    if 16 <= idade < 18 or idade >= 70:  # Regras corretas da legislação brasileira
        situacao = f"Com {idade} anos: VOTO OPCIONAL"
    elif idade >= 18:
        situacao = f"Com {idade} anos: VOTO OBRIGATÓRIO"
    else:
        situacao = f"Com {idade} anos: NÃO VOTA"
    
    return situacao

# Programa principal
ano = int(input("Ano de nascimento: "))
print(voto(ano))