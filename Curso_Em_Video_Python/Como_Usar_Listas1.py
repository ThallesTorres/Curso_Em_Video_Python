num = [2, 5, 9, 1]  # Listas são mutáveis
print(f'Lista - Original = {num}')

num[2] = 3  # Troca elementos, mas não pode adicionar elementos
print(f'Lista - Trocando um elemento = {num}')

num.append(7)  # Adiciona elementos
print(f'Lista - Adicionando um elemento = {num}')

num.insert(2, 2)  # Insere o 2 na posição 2, jogando os demais elementos para o lado
print(f'Lista - Inserindo um elemento = {num}')

num.remove(2)  # Remove o primeiro elemento 2 que encontrar
print(f'Lista - Removendo um elemento = {num}')

num.pop(2)  # Elimina o elemento na posição 2, se deixar sem nada ele remove o último elemento
print(f'Lista - Eliminando um elemento = {num}')

num.sort()  # Coloca a lista em ordem crescente (mudança não temporária)
print(f'Lista - Colocando a lista em ordem crescente = {num}')

num.sort(reverse=True)  # Coloca a lista em ordem decrescente (mudança não temporária)
print(f'Lista - Colocando a lista em ordem decrescente = {num}')

print(f'Lista - Contando os elementos = {len(num)}')

print('\nExemplos de uso: ')

print('Ex 01 - ')
if 5 in num:
    num.remove(5)
else:
    print('Não achei o número 5')
print(num)

print('\nEx 02 - ')
for n in num:
    print(f'{n}... ', end='')

print('\n\nEx 03 - ')
for pos, n in enumerate(num):
    print(f'Na posição {pos} encontrei o valor {n}')
print('Final')

print('\nEx 04 - ')
num = []
for cont in range(0, 5):
    num.append(int(input('Digite um valor: ')))
print(num)

print('\nEx 05 - ')
a = [2, 3, 4, 7]
b = a  # Ao se igualar, o python criar uma ligação entre elas
b[2] = 8
print(f'Lista A = {a}')
print(f'Lista B = {b}')

print('\nEx 06 - ')
a = [2, 3, 4, 7]
b = a[:]  # Copia os elementos, não faz uma ligação
b[2] = 8
print(f'Lista A = {a}')
print(f'Lista B = {b}')
