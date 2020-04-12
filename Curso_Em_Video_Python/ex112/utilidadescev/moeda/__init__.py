def escreva(msg):
    x = len(msg) + 4
    print("-" * x)
    print(f"--{msg}--")
    print("-" * x)
    
    
def resumo(preco=0, aumenta=15, diminui=12):
    print()
    print(f"{'--ANÁLISE--':^35}")
    
    print('-' * 35)
    
    print(f"Metade de {moeda(preco)}: \t{metade(preco, True)}")
    print(f"Dobro de {moeda(preco)}: \t{dobro(preco, True)}")
    print(f"Aumentado em {aumenta}%: \t{aumentar(preco, aumenta, True)}")
    print(f"Diminuido em {diminui}%: \t{diminuir(preco, diminui, True)}")
    
    print('-' * 35)
    
    
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
