# Ex: 101 - Crie um programa que tenha uma função chamada voto() que vai 
# receber como parãmetro o ano de nascimento de uma pessoa, retornando um 
# valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL ou 
# OBRIGATÓRIO nas eleições.

def voto(ano):
    from datetime import date
    

    idade = date.today().year - ano
    
    print("\n--Dados finais")
    print("Idade:", idade)
    
    if idade < 16:
        return "Situação do voto: NEGADO"
    
    elif idade in range(18, 66):
        return "Situação do voto: OBRIGATÓRIO"
    
    else:
        return "Situação do voto: OPCIONAL"


print('''
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
--Seja bem-vindo! 
--Exercício 101
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
''')

ano = int(input("Ano de nascimento: "))
print(voto(ano))

print('''
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
--Obrigado pelo uso!
--Desenvolvido por Thalles Torres
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-''')
