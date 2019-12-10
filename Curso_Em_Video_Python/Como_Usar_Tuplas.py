lanche = ('Hambúrguer', 'Suco', 'Pizza', 'Pudim', 'Batata Frita')
print(lanche[1])
print(lanche[-1])
print(lanche[1:3])
print(lanche[2:])
print(lanche[:2])
print(lanche[-2:])
print(lanche)

# Tuplas são imutáveis!!!
# lanche[1] = 'Refrigerante'
# print(lanche[1])

print('-' * 30)
for comida in lanche:
    print(f'Eu vou comer {comida}')
print('Comi pra caramba!')

print('-' * 30)
for cont in range(0, len(lanche)):
    print(f'Eu vou comer {lanche[cont]} na posição {cont}')
print('Comi pra caramba!')

print('-' * 30)
for pos, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na posição {pos}')
print('Comi pra caramba!')

print('-' * 30)
print(sorted(lanche))
print(lanche)

print('-' * 30)
a = (2, 5, 4)
b = (5, 8, 1, 2)
c = a + b
print(c)
c = b + a
print(c)

print('-' * 30)
print(c)
print(c.count(5))
print(c.index(5, 1))
print(c.index(2))
print(c.index(1))

print('-' * 30)
pessoa = ('Gustavo', 34, 'M', 33.55)
print(pessoa)
del(pessoa) # Só pode deletar a tupla inteira
print(pessoa)
