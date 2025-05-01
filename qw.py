#aula_numpy.py

import numpy as np

array_letras = np.array(['a','b','c','d','e'])

print(array_letras)

#Acessando posiçao especificar
print(array_letras[0])
#acessando partes do array
print(array_letras[0:2])

#criando um array de inteiros
precos = np.array([20,40,25,35,30])
print('Preços',precos)
#aumentando o preço de todos os valores do array em em 10%
novos_precos = precos * 1.1
print('Valor aumentado:>',novos_precos)

#soma de todos os preçox do array preços

total_venda = np.sum(precos)
print('Soma de todos os valores do array:',total_venda)

#media dos preços 
media_valor = np.mean(precos)
print('A media de preços do array:>',media_valor)

#Maior e menor valor do array
maior_valor = np.max(precos)
menor_valor = np.min(precos)
print('Maior preço do array:>',maior_valor)
print('Menor preço do array:>',menor_valor)

#NÃO FAÇA
#k = list(range(1,30))
#print(k)

#gerador de numeros aleatorios
rng = np.random.default_rng()
print('..!Aleatorios com Random!...')
print(rng.random(4_0)*100)


#Exercicio
#Gere 500.000 numeros  aleatorios
#mostre o maior e menor valor do array
#mostra a media dos valores
array_brincando = np.array(rng.random(500_000)*4_000)
print('\nARRAY',array_brincando)

maior_v = np.max(array_brincando)
menor_v = np.min(array_brincando)
print('Maior preço do array:>',maior_v)
print('Menor preço do array:>',menor_v)

media_v = np.mean(array_brincando)
print('A media de preços do array:>',media_v)