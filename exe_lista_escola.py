
#MINHA LISTA VAZIA DO MATERIA
listav_material_escola = []
#ADICI0NANDO MINHA LISTA DE VALORES
lista_valor_material = []
#ADICINANDO MINHA LISTA MATERIAL
for cont in range(2):
    material = input('ADICIONE SEU MATERIAL:')
    listav_material_escola.append(material)
    valores = float(input('ADICIONE O VALOR:'))
    lista_valor_material.append(valores)
#MOSTRANDO ;MINHA LISTA DE MATERIAL E VALORES
print('!MINHA LISTA Material ESCOLA e VALORES!')
for k in range(2):
    print('material:',listav_material_escola[k],'valor:',lista_valor_material[k])

m = max(lista_valor_material)
print(m)
indce = lista_valor_material.index(m)
print(indce)
Maior = listav_material_escola[indce]

print(Maior)



