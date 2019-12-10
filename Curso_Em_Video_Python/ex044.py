# Ex: 044 - Elaborar um programa que calcule o valor a ser pago por um
# produto, considerando o seu preço normal e condeção de pagamento:
# À vista dinheiro/cheque - 10% de desconto; À vista no cartão - 5% de
# desconto; Em até 2x no cartão - preço normal; 3x ou mais no cartão -
# 20% de juros.

print('-=-' * 10)
print('--Seja Bem Vindo'
      '\n--Exercício 44')
print('-=-' * 10, '\n')

print('--Valor Final da Mercadoria\n'
      '--Preencha os Dados')
valor_produto = float(input('Valor do Produto: R$'))
print('''\nFormas de Pagamento:
    [ 1 ] À vista (dinheiro/cheque) = 10% de desconto 
    [ 2 ] À vista (cartão) = 5% de desconto
    [ 3 ] Em até 2x no cartão = Preço normal
    [ 4 ] 3x ou mais no cartão = 20% de juros''')
condicao_pagamento = int(input('Digite a opção: '))
print('')

if condicao_pagamento > 4:
    print('Condição Inválida. Tente Novamente.')

else:
    if condicao_pagamento == 1:
        desconto = valor_produto * 10 / 100
        valor_final = valor_produto - desconto
        print(f'--Dados Finais\n'
              f'Preço Inicial:          R${valor_produto}\n'
              f'Desconto:               R${desconto:.2f}\n'
              f'Preço Final:            R${valor_final:.2f}')

    elif condicao_pagamento == 2:
        desconto = valor_produto * 5 / 100
        valor_final = valor_produto - desconto
        print(f'--Dados Finais\n'
              f'Preço Inicial:          R${valor_produto}\n'
              f'Desconto:               R${desconto:.2f}\n'
              f'Preço Final:            R${valor_final:.2f}')

    elif condicao_pagamento == 3:
        desconto = 0
        valor_final = valor_produto
        preco_parcelado = valor_final / 2
        print(f'--Dados Finais\n'
              f'Preço Inicial:          R${valor_produto}\n'
              f'Desconto:               Sem Desconto\n'
              f'Preço das Parcelas:     R${preco_parcelado:.2f} (2x)\n'
              f'Preço Final:            R${valor_final:.2f}')

    else:
        parcelas = int(input('Quantidade de parcelas: '))
        juros = valor_produto * 20 / 100
        valor_final = valor_produto + juros
        preco_parcelado = valor_final / parcelas
        print(f'--Dados Finais\n'
              f'Preço Inicial:          R${valor_produto}\n'
              f'Total de Juros:         R${juros:.2f}\n'
              f'Preço das Parcelas:     R${preco_parcelado:.2f} ({parcelas}x)\n'
              f'Preço Final:            R${valor_final:.2f}')

print('')
print('-=-' * 10)
print('--Obrigado Pelo Uso'
      '\n--Desenvolvido por Thalles')
print('-=-' * 10, '\n')
