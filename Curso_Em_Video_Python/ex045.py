# Ex: 045 - Crie um programa que faça o computador jogar JOKENPÔ com você.

from random import randint

print('''
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
--Seja bem-vindo! 
--Exercício 045
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
''')

print('--Jogo: Pedra, Papel ou tesoura')
print('''--Você acha que consegue ganhar de mim?!! Tente!!
    [ 1 ] Para Pedra
    [ 2 ] Para Papel
    [ 3 ] Para Tesoura''')
opcao = int(input('Qual você irá escolher? '))
print('')

if opcao > 3:
    print('Opção Inválida. Tente Novamente')

else:
    lista = ('Pedra', 'Papel', 'Tesoura')
    sorteado = randint(0, 2)

    if sorteado == 0:
        if opcao == 2:
            print(f'Droga!! Você ganhou, eu tinha escolhido {lista[sorteado]}')

        elif opcao == 1:
            print(f'Droga, empatamos, eu tinha escolhido {lista[sorteado]}')

        else:
            print(f'Eba!! Ganhei, eu tinha escolhido{lista[sorteado]}')

    elif sorteado == 1:
        if opcao == 3:
            print(f'Droga!! Você ganhou, eu tinha escolhido {lista[sorteado]}')

        elif opcao == 2:
            print(f'Droga, empatamos, eu tinha escolhido {lista[sorteado]}')

        else:
            print(f'Eba!! Ganhei, eu tinha escolhido{lista[sorteado]}')

    else:
        if opcao == 1:
            print(f'Droga!! Você ganhou, eu tinha escolhido {lista[sorteado]}')

        elif opcao == 3:
            print(f'Droga, empatamos, eu tinha escolhido {lista[sorteado]}')

        else:
            print(f'Eba!! Ganhei, eu tinha escolhido {lista[sorteado]}')

print('''
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
--Obrigado pelo uso!
--Desenvolvido por Thalles Torres
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-''')
