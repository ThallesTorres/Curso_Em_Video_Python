# Ex: 039 - Faça um programa que leia o ano de nascimento de um jovem e
# informe, de acordo com sua idade: Se ele ainda vai se alistar ao serviço
# militar, Se é a hora de se alistar, Se já passou do tempo do alistamento.
# Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

from datetime import date

print('''
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
--Seja bem-vindo! 
--Exercício 039
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
''')

print('--Serviço Militar OBRIGATÓRIO!!! ')
print('--Preencha os Dados ')
print('''Qual é o seu Gênero: 
      [ M ] Para Masculino
      [ F ] Para Feminino''')
sexo = input('').upper()

if sexo != 'M' and sexo != 'F':
      print('Gênero Inválido!')

elif sexo == 'F':
      print('Você não é OBRIGADA a comparecer ao Alistamento Militar. ')

else:
      ano_nasc = int(input('Ano de nascimento: '))
      ano_atual = date.today().year
      idade = ano_atual - ano_nasc
      print(f'\nQuem nasceu em {ano_nasc} tem {idade} anos em {ano_atual}.')

      if idade > 18:
            atrasado = idade - 18
            print(f'Atrasado {atrasado} anos para o Alistamento OBRIGATÓRIO. \n'
                  f'Seu Alistamento foi em {ano_atual - atrasado}.')

      elif idade == 18:
            print(f'Já pode comparecer ao Alistamento Militar.')

      else:
            falta = 18 - idade
            print(f'Falta {falta} anos para o Alistamento OBRIGATÓRIO. \n'
                  f'Seu alistemento será em {falta + ano_atual}.')

print('''
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
--Obrigado pelo uso!
--Desenvolvido por Thalles Torres
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-''')
