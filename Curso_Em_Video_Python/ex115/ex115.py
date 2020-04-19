# Ex: 115 - Crie um pequeno sistema modulorizado que permita cadastrar pessoas 
# pelo seu nome e idade em um arquivo de texto simples. O sistema só vai ter 2 
# opções: cadastrar uma nova pessoa e listar todas as pessoas cadastradas.

from Bibliotecas import *


print('''
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
--Seja bem-vindo! 
--Exercício 115
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
''')

x = True
while x:   
    opcao = menu()
    
    if opcao == 1:
        ver()
        
    elif opcao == 2:
        cadastrar()
        
    elif opcao == 3:
        x = sair()

print('''
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
--Obrigado pelo uso!
--Desenvolvido por Thalles Torres
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-''')
