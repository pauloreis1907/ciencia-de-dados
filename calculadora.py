#calculadora
#2 x 4 = 9
#2 x 5 = 10
#multiplicador x contador = produto
contador = 0
multiplicador = int(input('informe o multiplicado:'))
while contador <= 10:
    produto = multiplicador * contador
    print(multiplicador, 'X', contador, '=', produto)
    contador = contador + 1
    
print('FIM !!!')