# DESAFIO 105
# Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e vai retornar um dicionário com as seguintes informações:
# - Quantidade de notas
# - A maior nota
# - A menor nota
# - A média da turma
# - A situação (opcional)
# Adicione também as docstrings da função.

def notas(* resultados, sit = False):
    """_summary_
    → Função para analisar notas e situações de vários alunos.

    Args:
        resultados: uma ou mais notas dos alunos. Aceita várias.
        sit (bool, optional): indicando se deve ou não mostrar a situação da turma. Defaults to False.

    Returns:
        _type_: dicionário com várias informações sobre a situação da turma.
    """
    boletim = {}
    boletim['Quantidade de notas'] = len(resultados)
    boletim['Maior nota'] = max(resultados)
    boletim['Menor nota'] = min(resultados)
    boletim['Média das notas'] = sum(resultados)/len(resultados)
    
    if sit:
        if boletim['Média das notas'] < 4:
            sit = 'HORRÍVEL'
        elif boletim['Média das notas'] < 5:
            sit = 'RUIM'
        elif boletim['Média das notas'] < 6:
            sit = 'OK'
        elif boletim['Média das notas'] < 7:
            sit = 'BOA'
        elif boletim['Média das notas'] < 9:
            sit = 'ÓTIMA'
        else:
            sit = 'ESPETACULAR'
        boletim['Situação'] = sit
    
    return boletim
    


historico = notas(5, 7, 9.6, sit = True)
print(historico)
