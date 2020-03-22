# Ex: 083 - Crie um programa onde o usuário digite uma expressão qualquer que use
# parênteses. Seu aplicativo deverá analisar se a expressão passada está com os 
# parênteses abertos e fechado na ordem correta.

print('-=-' * 10)
print('--Seja Bem Vindo'
      '\n--Exercício 83')
print('-=-' * 10, '\n')

expre = input(f'Digite a expressão com parênteses: ')
teste = []

for x in expre:
      if x == '(':
            teste.append(x)
      elif x == ')':
            if len(teste) > 0:
                  teste.pop()
            else:
                  teste.append(x)
                  break

if len(teste) == 0:
      print('A expressão é válida')
else:
      print('A expressão não é válida')

print('''
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
--Obrigado Pelo Uso!!
--Desenvolvido por Thalles Torres
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-''')
