# Ex: 106 - Faça um mini-sistema que utilize o Interactive Help do Python. 
# O usuário vai digitar o comando e o manual vai aparecer. 
# Quando o usuário digitar a palavra 'FIM', o programa se encerrará.

def escreva(msg):
    x = len(msg) + 4
    print(">" * x)
    print(f">>{msg}>>")
    print(">" * x)
    
def ajuda(x):
    print(help(x))


print('''
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
--Seja bem-vindo! 
--Exercício 106
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
''')

escreva("SISTEMA DE AJUDA DO PYTHON")

while True:
    x = input("Função ou Biblioteca > ")
    
    if x.lower() == 'fim':
        break
    else:
        ajuda(x)

print('''
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
--Obrigado pelo uso!
--Desenvolvido por Thalles Torres
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-''')
