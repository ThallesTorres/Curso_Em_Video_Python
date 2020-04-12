def leiaDinheiro(msg):
    while True:
        valor = input(msg).strip().replace(',', '.')

        temp = valor

        if temp.replace('.', '').isnumeric():
            return float(valor)
        
        print("\033[31mValor Inválido\033[m\n")