#aula_lista.py
#Iniciando uma lista vazia

listaVazia = []
print('lista vazia ',listaVazia)

#Iniciando uma lista de valores inteiros
listaInteiros = [2,4,5,6,9]
print('Lista de Inteiros:', listaInteiros)

#Iniciando uma lista de valores Reias
listaReais = [9.8,6.5,2.1,3.02,7.7]
print('Lista de Reias:', listaReais)

#Iniciando uma lista de valores string
listaFrutas = ['Abacaxi','cupu','Ameixa','castanha','sapota']
print('Lista de Frutas:', listaFrutas)
#adicionar valores a lista usando appende
listaFrutas.append('araça')
print('Lista de Frutas:', listaFrutas)
listaFrutas.append('camu-camu')
print('Lista de Frutas:', listaFrutas)
#para saber  o tamanho lista uando o lenght de forma abreviada le
tamanhoListaFrutas = len(listaFrutas)
print('a lista de frutas possui',tamanhoListaFrutas)
#mostra um valor especifico
print(listaFrutas[3])
#altera valor da lista 
listaFrutas[1] = 'acai'
print(listaFrutas)

#excluindo um valor da lista
#del listaFrutas[4]
listaFrutas.pop(4)
print(listaFrutas)

#Manipulando lista com while
z = 0
tamanhoListaFrutas = len(listaFrutas)

while z < tamanhoListaFrutas:
    print('Valor na posiçao',z,'é:',listaFrutas[z])
    z=z+1
    
    
#Manipulado lista com For
for fruta in listaFrutas:
    print('FOR',fruta)
  
  
  
    
#Manipulado lista com For
for fruta in listaFrutas:
    if fruta.upper() == 'cupu'.upper():
        print('Fruta Encontrada:',fruta)
        
nome = 'mariA'

print(nome.upper())