# Ex: 087 - Aprimore o desafio anterior, mostrando no final: A- A soma de todos os 
# valores pares digitados. B- A soma dos valores da terceira coluna. C- O maior valor 
# da sugunda linha.

print('''
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
--Seja bem-vindo! 
--Exercício 087
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
''')

matriz = [[], [], []]
maior_valor_2_linha = soma_3_coluna = soma_par = 0

for linha in range(3):
    for coluna in range(3):
        x = int(input(f"Valor para [{linha}, {coluna}]: "))
        matriz[linha].append(x)
        
        soma_par += x if x % 2 == 0 else 0 
        soma_3_coluna += x if coluna == 2 else 0
        maior_valor_2_linha = x if linha == 1 and maior_valor_2_linha < x else maior_valor_2_linha
                
print("\n--matriz")
for linha in range(3):
    for coluna in matriz[linha]:
        print(f"[{coluna: ^ 5}] ", end='')
    print()

print(f'''\n--Dados finais
Soma dos valores pares: {soma_par}
Soma dos valores da 3º coluna: {soma_3_coluna}
Maior valor da 2º linha: {maior_valor_2_linha}''')

print('''
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
--Obrigado pelo uso!
--Desenvolvido por Thalles Torres
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-''')
