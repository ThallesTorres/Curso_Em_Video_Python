# Ex: 073 - Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do
# Campeonato Brasileiro de Futebol, na ordem da colocação. Depois mostre: Apenas
# os 5 primeiros colocados; Os últimos 4 colocados da tabela; Uma lista com os
# times em ordem alfabética; Em que posição na tabela está o time da Chapecoense.

print('''
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
--Seja bem-vindo! 
--Exercício 073
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
''')

times = ('Flamengo', 'Santos', 'Palmeiras', 'Corinthians', 'São Paulo',
         'Internacional', 'Bahia', 'Atlético-MG', 'Atlético-PR', 'Botafogo',
         'Grêmio', 'Ceará', 'Fortaleza', 'Goiás', 'Vasco', 'Cruzeiro',
         'Fluminense', 'CSA', 'Chapecoense', 'Avaí')

print(f'''--Dados Finais
Lista de Times: {times}
----
5 Primeiros Colocados: {times[:5]}
----
Últimos 4 Colocados: {times[-4:]}
----
Ordem Alfabética: {sorted(times)}
----
Posição Chapecoense: {times.index('Chapecoense') + 1}° Colocado''')

print('''
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
--Obrigado pelo uso!
--Desenvolvido por Thalles Torres
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-''')
