import pandas as pd

#inportando uma base de dados
vendas_df = pd.read_csv('Contoso - vendas - 2017.csv', sep=';')
promocoes_df = pd.read_csv('Contoso - Promocoes.csv', sep=';', encoding='latin-1')
lojas_df = pd.read_csv('Contoso - Lojas.csv', sep=';', encoding='latin-1')
clientes_df = pd.read_csv('Contoso - Clientes.csv', sep=';', encoding='latin-1')
produto_df = pd.read_csv('Contoso - Cadastro Produtos.csv', sep=';', encoding='latin-1')
#print(vendas_df)
print(vendas_df.info())
print(promocoes_df.info())
print(lojas_df.info())
print(clientes_df.info())
print(produto_df.info())

clientes_df.rename({'ID Cliente':'ID Cliente'})
novo_df = vendas_df.merge(clientes_df, on='ID Cliente')

print(novo_df)

#visualizaçao
#print(vendas_df['Data da Venda'])
#print(vendas_df[:3])

#print(vendas_df['Data da Venda'][2])