#aula sobre dicionario no python

# os principais elemento sintaticos são {} chaves, virgulas : dois pontos
#em dicionarios temos o conceito de CHAVE:VALOR
#criando um dicionario vazio 
#note que nas listas usamos os  colchetes[]
dicionario_vazio = {}

#criando um dicionario com valores

dicio_preenchido = {'nome':'carlos',
                    'idade':21,
                    'altura':1.65}
print(dicio_preenchido)

#acessando  o valor de uma CHAVE em especifico
aux_nome = dicio_preenchido['nome']
print('mostrando o valor da chave nome:',aux_nome)
#acessando uma chave  especifico que nao existe 
profissao = dicio_preenchido.get('prof','nao encontrado')
print(profissao)
#para adicionar ou modificar um elemento nop dicionario usando atribuiçao
dicio_preenchido['idade'] = 30
print('altera a idade:',dicio_preenchido)
#adicionando uma nova chave e valor
dicio_preenchido['profisao'] = 'motoqueiro'
print('incluindo um nova chaver-valor:',dicio_preenchido)
#removendo um elemento especifico
aux_idade = dicio_preenchido.pop('idade')
print('idade removida >',dicio_preenchido)
print('mesmo removido podemos guardar o valor em outro local:',aux_idade)

#Para excluir o dicionario usando o comando del
#por motivos de segiranca não usaremos o comando

#quando pegamos um dicionario que não sabemos as benditas chaves
#temos um forma facil de identificar  usando a funçaõ keys
todas_chaves = dicio_preenchido.keys()
print('Todas as chaves do dicionario:',todas_chaves)
#temos uma  facil de identificar os valores , esando a fução values
todas_chaves = dicio_preenchido.values()
print('Todas as chaves do dicionario:',todas_chaves)

#podemos fazer interaçao no dicionario de forma individual o par chave-valor
for chave,valor in dicio_preenchido.items():
    print(chave,'-',valor)