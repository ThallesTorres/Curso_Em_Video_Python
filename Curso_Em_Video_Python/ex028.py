# Ex: 028 - Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.
from random import randint
from time import sleep #Faz o computador "dormir"
from termcolor import colored #Muda a cor
print(colored('/-/-' * 20, 'blue'))
print(colored('Vou pensar em um número entre 0 e 5. Tente adivinhar...', 'red'))
print(colored('/-/-' * 20, 'blue'))
n = int(input('Em que número eu pensei? '))
print('PROCESSANDO...')
sleep(2)
escolhido = randint(0, 5) #Comando para o computador pegar um número aleatório inteiro
if escolhido == n:
    print('PARABÉNS!! Você conseguiu me vencer!')
else:
    print(f'GANHEI!! Eu pensei no número {escolhido} e não no {n}!')
