# Ex: 105 - Faça um programa que tenha uma função notas() que pode receber 
# várias notas de alunos e vai retornar um dicionário com as seguintes 
# informações: 
# -Quantidade de notas; 
# -A maior nota; 
# -A menor nota; 
# -A média da turma; 
# -A situação (opcional).
# Adicione também as docstrings da função.

def notas(* notas, situacao=False):
    '''
    => Análisador de notas.
    :param notas: Notas a serem analisadas fornecidas pelo usuário.
    :param situacao: (opcional) Situação medida atraves da média.
    :return: Dicionário com as analises feitas.
    '''
    
    notas_dict = dict()
    
    # media = quantidade = 0
    # for cont, nota in enumerate(notas):
    #     quantidade += 1
    #     media += nota
        
    #     if cont == 0:
    #         menor = nota
    #         maior = nota
            
    #     else:
    #         if menor > nota:
    #             menor = nota
            
    #         if maior < nota:
    #             maior = nota 
            
    
    notas_dict['Quantidade'] = len(notas)
    notas_dict['Maior'] = max(notas)
    notas_dict['Menor'] = min(notas)
    notas_dict['Media'] = sum(notas) / notas_dict['Quantidade']
    
    if situacao:
        if notas_dict['Media'] < 5:
            notas_dict['Situacao'] = 'Ruim'

        elif notas_dict['Media'] >= 7:
            notas_dict['Situacao'] = 'Boa'
        
        else:
            notas_dict['Situacao'] = 'RAZOÁVEL'
    
    return notas_dict



print('''
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
--Seja bem-vindo! 
--Exercício 105
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
''')

print(notas(2,3,4,5,6,7,8,9, situacao=True))
help(notas)

print('''
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
--Obrigado pelo uso!
--Desenvolvido por Thalles Torres
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-''')
