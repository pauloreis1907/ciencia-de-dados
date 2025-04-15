import pandas as pd
import matplotlib.pyplot as plt

dadosProdutos = pd.read_csv('mmmm.csv', delimiter=',')

indice = dadosProdutos['num2023'].idxmax()
indice2 = dadosProdutos['num2023'].idxmin()
#obtendo o indece maior e menor
estado_com_maior = dadosProdutos.loc[indice,'EstadosBR']   
estado_com_menor = dadosProdutos.loc[indice2,'EstadosBR']

print(dadosProdutos)


p = dadosProdutos.loc[indice,'num2023']
p2 = dadosProdutos.loc[indice2,'num2023']
#cor = ['#0000FF','pink','#00FFFF','#A52A2A','#5F9EA0','#F0F8FF','#F0FBff','#F8F8FF','#FFFAFA']

print('\nEstado com maior numero de morte:',estado_com_maior,'com', p)
print('\nEstado com menor numero de morte:', estado_com_menor,'com', p2)
#apresetando grafico


labels = dadosProdutos['EstadosBR']
sizes = dadosProdutos['num2023']

figl,axl = plt.subplots()

axl.pie(sizes,labels=labels,autopct='%1.1f%%', shadow= True, startangle=90)

axl.axis('equal')
plt.suptitle('FONTE:https://g1.globo.com/politica/noticia/2024/03/07/brasil-feminicidios-em-2023.ghtml\n')
plt.title('Feminicídios em todos os estados brasileiros\n')

plt.show()