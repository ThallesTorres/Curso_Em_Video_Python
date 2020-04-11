def escreva(msg):
    x = len(msg) + 4
    print("-" * x)
    print(f"--{msg}--")
    print("-" * x)
    print()
    

def dobro(numero):
    return numero * 2


def metade(numero):
    return numero / 2


def aumentar(numero, taxa):
    return numero + numero * taxa /100


def diminuir(numero, taxa):
    return numero - numero * taxa /100
