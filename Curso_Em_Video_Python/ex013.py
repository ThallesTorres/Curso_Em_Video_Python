salario = float(input('Digite o salário: R$'))
aumento = float(input('Digite a porcentagem do aumento: '))
total = salario * aumento / 100
input(f'Aumento: R${total:.2f} \nAumento + Salário: R${total + salario:.2f} ')
