# Ex: 097 - Faça um programa que tenha uma função chamada escreva(), que 
# receba um texto qualquer como parâmetro e mostre uma mensagem com tamanho 
# daptável.

def escreva(msg):
    print("\n--Dados finais:")
    x = len(msg) + 2
    print(">" * x)
    print(f" {msg} ")
    print(">" * x)


print('''
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
--Seja bem-vindo! 
--Exercício 097
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
''')

print("--Preenche:")
msg = input("Mensagem: ")
escreva(msg)

print('''
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
--Obrigado pelo uso!
--Desenvolvido por Thalles Torres
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-''')
