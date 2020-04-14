# Ex: 114 - Crie um código em Python que teste se o site Pudim está acessivel 
# pelo computador usado.

def printred(msg):
    print(f"\033[31m{msg}\033[m")


def sitePudim(x="pudim.com.br"):
    import requests
    
    
    site = x.replace('http://', '')
    
    try:
        site = requests.get(f"http://{site}")
    
    except Exception as erro:
        printred(f"O Site {x} está offiline.\nErro: {erro.__class__}")
        
    else:
        printred(f"O Site {x} está online.")


print('''
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
--Seja bem-vindo! 
--Exercício 114
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
''')

sitePudim(input("Digite o site: "))

print('''
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
--Obrigado pelo uso!
--Desenvolvido por Thalles Torres
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-''')
