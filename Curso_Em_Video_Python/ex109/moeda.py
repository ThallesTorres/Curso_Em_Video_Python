def escreva(msg):
    x = len(msg) + 4
    print("-" * x)
    print(f"--{msg}--")
    print("-" * x)
    print()
    
    
def moeda(numero=0, moeda='R$'):
    return f'{moeda}{numero:.2f}'.replace('.', ',')
    

def dobro(numero=0, formatado=True):
    x = numero * 2

    return x if not moeda else moeda(x)


def metade(numero=0, formatado=True):
    x = numero / 2
    
    return x if not moeda else moeda(x)


def aumentar(numero=0, taxa=0, formatado=True):
    x = numero + numero * taxa /100
    
    return x if not moeda else moeda(x)


def diminuir(numero=0, taxa=0, formatado=True):
    x = numero - numero * taxa /100
    
    return x if not moeda else moeda(x)
