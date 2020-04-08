# Ex: 104 - Crie um programa que tenha a função leiaInt(), que vai funcionar 
# de forma semelhante á função input() do Python, só que fazendo a validação 
# para aceitar apenas um valor numérico.

def leiaInt(str):
    '''
    => Verificador de valores 
    '''
    
    while True:
        num = input(str).strip()
        if not num.isnumeric():
            print("--Valor Inválido.")
        else:
            return num


print('''
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
--Seja bem-vindo! 
--Exercício 104
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
''')

num = leiaInt("Digite um número: ")
print(f"Número digitado: {num}")

print('''
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
--Obrigado pelo uso!
--Desenvolvido por Thalles Torres
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-''')
