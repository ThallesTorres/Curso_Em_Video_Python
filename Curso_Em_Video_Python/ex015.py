d = int(input('Quantidade de Dias alugado: '))
km = float(input('Quantidade de Km percorridos: '))
precod = d * 60
precokm = km * 0.15
print('-' * 5, 'Preços', '-' * 5, f'\nDia: R${precod:.2f} \nKm: R${precokm:.2f} \nTotal: R${precod + precokm:.2f}')