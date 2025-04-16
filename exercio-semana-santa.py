lista = []

for cont in range(3):
    peixe = input('lista seu peixes da semana  santa usando a virgula :')
    lista.append(peixe)

print('LISTA QUE VOCE GOSTA')
print(lista)

cont = 0
while cont < 3 :
    if lista[cont] == 'tambaqui'.lower():
      del lista[cont]
      
    cont = cont + 1
   
 #if 'tambaqui' in lista:
  #  lista.remove('tambaqui')

print(lista)