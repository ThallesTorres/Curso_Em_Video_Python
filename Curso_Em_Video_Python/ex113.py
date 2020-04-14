# Ex: 113 - Reescreva a função leiaInt() que fizemos no desafio 104, incluindo 
# agora a possibilidade da digitação de um número de tipo inválido. Aproveite 
# e crie também uma função leiaFloat() com a mesma funcionalidade. 

def printred(msg):
    print(f"\033[31m{msg}\033[m")


def leiaInt(msg):
    '''
    => Verificador de valores 
    '''
    
    while True:      
        try:
            num = int(input(msg))
            
        except (TypeError, ValueError):
            printred("--Tipo de dado digitado inválido.")
        
        except Exception as erro:
            printred(f"--Erro desconhecido.\n{erro.__class__}")
        
        else:
            return num
        
        finally:
            print()
    

def leiaFloat(msg):
    while True:
        try:
            num = float(input(msg).replace(",", "."))
            
        except (TypeError, ValueError):
            printred("--Tipo de dado digitado inválido.")

        except Exception as erro:
            printred(f"--Erro ,{erro.__class__}")
        
        else:
            return num
        
        finally:
            print()


print('''
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
--Seja bem-vindo! 
--Exercício 113
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
''')

numInt = leiaInt("Digite um número inteiro: ")
numFloat = leiaFloat("Digite um número real: ")
print(f"Número inteiro digitado: {numInt}")
print(f"Número real digitado: {numFloat}")


print('''
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
--Obrigado pelo uso!
--Desenvolvido por Thalles Torres
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-''')
