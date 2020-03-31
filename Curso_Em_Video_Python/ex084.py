# Ex: 084 - Faça um programa que leia nome e peso de várias pessoas, guardando tudo
# em uma lista. No final, mostre: A) Quantas pessoas foram cadastradas. B) Uma 
# listagem com as pessoas mais pesadas. C) Uma listagem com as pessoas mais leves.

print('''
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
--Seja bem-vindo! 
--Exercício 084
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
''')

temp = list()
princ = list()

while True:
    print("--Preencha ")
    temp.append(str(input("Nome: ").capitalize().strip()))
    temp.append(float(input("Peso [Kg]: ").strip()))
    # princ.append(str(input("Nome: "))
    #              float(input("Peso: ")))
    
    if len(princ) == 0:
        pesado = leve = temp[1]
        
    else:
        if pesado < temp[1]:
            pesado = temp[1]
            
        if leve > temp[1]:
            leve = temp[1]
    
    princ.append(temp[:])
    temp.clear()
    
    resp = input("\nDeseja adicionar outra pessoa? [S/N] ").strip().lower()
    print()
    if "n" in resp:
        break
        
print(f"""--Dados finais
Total de pessoas cadastradas: {len(princ)}
Mais pesado(s) {''.join(f'[{pessoa[0]}] ' for pessoa in princ if pessoa[1] == pesado)}com {pesado}Kg
Mais leve(s) {''.join(f'[{pessoa[0]}] ' for pessoa in princ if pessoa[1] == leve)}com {leve}Kg""")

# # --Parte do 'join' sem ele:
# for pessoa in princ:
#     if pessoa[1] == pesado:
#         print(f'[{pessoa[0]}]')
        
# for pessoa in princ:
#     if pessoa[1] == leve:
#         print(f'[{pessoa[0]}]')

print('''
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
--Obrigado pelo uso!
--Desenvolvido por Thalles Torres
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-''')
