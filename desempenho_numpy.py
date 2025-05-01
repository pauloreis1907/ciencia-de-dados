import numpy as np
import time 

lista = list(range(1,10_000_001))
array_num = np.array(range(1,10_000_001))
#print(lista)

inicio = time.time()
soma_lista  = sum(lista)
fim = time.time()

print('Tempo execução LISTA:>',fim-inicio)

inicio = time.time()
soma_array = np.sum(array_num)
fim = time.time()

print('Tempo exercução NUMPY:>',fim-inicio)