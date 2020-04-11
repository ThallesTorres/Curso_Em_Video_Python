def escreva(msg):
    x = len(msg) + 4
    print("-" * x)
    print(f"--{msg}--")
    print("-" * x)
    print()
    
    
def moeda(numero=0, moeda='R$'):
    return f'{moeda}{numero:.2f}'.replace('.', ',')
    

def dobro(numero=0):
    return numero * 2


def metade(numero=0):
    return numero / 2


def aumentar(numero=0, taxa=0):
    return numero + numero * taxa /100


def diminuir(numero=0, taxa=0):
    return numero - numero * taxa /100
