# Ex: 114 - Crie um código em Python que teste se o site Pudim está acessivel 
# pelo computador usado.

def printred(msg):
    print(f"\033[31m{msg}\033[m")


def sitePudim(site):
    import requests
    
    
    if site == '': #Tive que adicionar esse if, pois colocando 'site="pudim.com.br"' não estava indo...
        site = "pudim.com.br"
    
    try:
        requests.get(f"http://{site.replace('http://', '')}")
    
    except Exception as erro:
        printred(f"O Site {site} está offiline.\nErro: {erro.__class__}")
        
    else:
        printred(f"O Site {site} está online.")


print('''
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
--Seja bem-vindo! 
--Exercício 114
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
''')

sitePudim(input("Digite o site [site padrão = pudim.com.br]: "))

print('''
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
--Obrigado pelo uso!
--Desenvolvido por Thalles Torres
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-''')
