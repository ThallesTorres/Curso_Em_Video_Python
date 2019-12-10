# Ex: 029 - Escreva um progrma que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, mostra uma mensagem dizendo que ele foi multado. A multa vai custar R$7 por cada Km acima do limite.
print('-' * 15)
print('-----Radar-----')
print('-' * 15)
velocidade = float(input('Digite a velocidade atual do carro (Km/h): '))
if velocidade > 80:
    print('Você foi multado por exceder a velocidade de 80Km/h.')
    multa = (velocidade - 80) * 7
    print(f'Pague a multa de R${multa:.2f}')
else:
    print('Dentro do limite de velocidade...')
print('Tenha um bom dia! Dirija com segurança! ')
