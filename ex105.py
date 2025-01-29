def notas(*notas, sit=False):
    """
    Analisa notas de alunos e retorna estatísticas.
    
    Parâmetros:
        *notas (float): Uma ou mais notas dos alunos (pode ser vazio).
        sit (bool, opcional): Define se inclui a situação da turma. Padrão: False.
    
    Retorna:
        dict: Dicionário com total de notas, maior, menor, média e situação (se solicitado).
    
    Levanta:
        ValueError: Se nenhuma nota for informada.
    """
    if not notas:
        raise ValueError("Nenhuma nota foi informada!")
    
    relatorio = {}
    relatorio['total'] = len(notas)
    relatorio['maior'] = max(notas)
    relatorio['menor'] = min(notas)
    relatorio['media'] = sum(notas) / len(notas)
    
    if sit:
        if relatorio['media'] >= 7:
            relatorio['situacao'] = 'BOA'
        elif relatorio['media'] >= 5:
            relatorio['situacao'] = 'RAZOÁVEL'
        else:
            relatorio['situacao'] = 'RUIM'
    
    return relatorio

# Exemplo de uso
try:
    resp = notas(7, 8, 9, 4, sit=True)
    print(resp)
except ValueError as e:
    print(e)