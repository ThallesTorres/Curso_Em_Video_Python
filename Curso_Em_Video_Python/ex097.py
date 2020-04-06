# Ex: 097 - Faça um programa que tenha uma função chamada escreva(), que 
# receba um texto qualquer como parâmetro e mostre uma mensagem com tamanho 
# daptável.

def escreva(msg):
    x = len(msg) + 2
    print(">" * x)
    print(f" {msg}")
    print(">" * x)


print('''
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
--Seja bem-vindo! 
--Exercício 097
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
''')

escreva("Tente escrever algo!!")
msg = input("Mensagem: ")
escreva(msg)

print('''
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
--Obrigado pelo uso!
--Desenvolvido por Thalles Torres
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-''')
