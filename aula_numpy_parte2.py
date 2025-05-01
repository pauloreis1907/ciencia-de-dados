import numpy as np

#---------outra aula------------
#geração de numeros inteiros aleatorios
#os paramentros são: valor mais baixo, valor mais alto e quantidade
#guardar no array
array_qualquer = np.array(np.random.randint(4,10,10))
print(array_qualquer)

#gerando uma matriz BI-dimensional (D2)
print('--- GERANDO MATRIX ---')
matriz_inteiros = np.array(np.random.randint(1, 10, size=(2,2)))
print(matriz_inteiros)

#verificando se um array contem valores vazio
print(np.isnan(array_qualquer))

#organizando os valores em ordem
print('EM ORDEM',np.sort(array_qualquer))
#organizando os valores em ordem decrescente
qualquer_decrescente =np.sort(array_qualquer)[::-1]
print('Em ordem descrescente:',(qualquer_decrescente))



array_d = np.array(np.random.randint(20,15_000, 900_000))
print('\n Meu array',array_d)

media_v = np.mean(array_d)
print('A media de preços do array:>',media_v)

p= array_d[0]
s=array_d[-1]

print('primeiro',p)
print('segundo',s)

m=np.max(array_d)
print('Maior',m)

me=np.min(array_d)
print('Menor',me)

print('EM ORDEM',np.sort(array_d))

#conta os valores unicos e suas repetçoes
valores_unicos, contagens = np.unique(array_d, return_counts=True)
for valor, cont in zip(valores_unicos,contagens):
    print(f'valor:{valor} - contagem:{cont}')