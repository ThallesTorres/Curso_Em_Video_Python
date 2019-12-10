preco = float(input('Valor do produto: '))
porcentagem = float(input('Porcentagem de desconto: '))
total = preco * porcentagem / 100
input(f'Desconto de: R${total:.2f} \nValor do produto com desconto: R${preco - total:.2f}')
