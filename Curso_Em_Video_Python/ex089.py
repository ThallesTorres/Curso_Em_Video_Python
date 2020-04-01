# Ex: 089 - Crie um programa que leia nome e duas notas de vários alunos e 
# guarde tudo em uma lista composta. No final, mostre um boletim contendo a 
# média de cada um e permita que o usuário possa mostrar as notas de cada 
# aluno individualmente.

print('''
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
--Seja bem-vindo! 
--Exercício 089
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
''')

princ = list()
# temp = list()
cont = 0

resp = 's'
while resp == 's':
    # temp.append(str(input("Nome do aluno: ")))
    # temp.append(int(input("Nota 1: ")))
    # temp.append(int(input("Nota 2: ")))
    
    # princ.append(temp[:])
    # temp.clear()

    princ.append([str(input("Nome do aluno: ")),
                 int(input("Nota 1: ")),
                 int(input("Nota 2: "))])
    
    while True:
        resp = input("Deseja adicionar mais um aluno? [S/N] ").lower()
        if resp in 'sn':
            break
        
print("--Dados finais \n n°     Nome       Média ")
for cont, aluno in enumerate(princ):
    print(f" {cont}{aluno[0]:^7}  {(aluno[1] + aluno[2]) / 2:^7}")

while True:
    resp = int(input("Nota do aluno ('999' para parar):"))
    
    if resp == 999:
        break
    
    print(f"Notas de {princ[resp][0]}: Nota 1 = {princ[resp][1]}; Nota 2 = {princ[resp][2]}")
    
print('''
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
--Obrigado pelo uso!
--Desenvolvido por Thalles Torres
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-''')
