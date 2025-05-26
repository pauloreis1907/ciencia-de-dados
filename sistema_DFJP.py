import os

alunos = []

#Diego Vulgor Léo Jardim
def cadastrar_aluno():
    nome = input('Nome do aluno: ')
    idade = int(input('Idade do aluno:'))

    notas = []

    for i in range(1, 5):
         while True: #Loop interno para garantir que uma nota válida seja inserida
            try:
                nota = float(input(f'Nota {i}: ')) #Solicita a nota
                if 0 <= nota <= 10: #Verifica se a nota está entre 0 e 10
                    notas.append(nota) #Adiciona a nota válida à lista de notas
                    break #Sai do loop while interno se a nota for válida
                else:
                    print('A nota deve ser entre 0 e 10. Tente novamente.') #Mensagem de erro para nota fora do intervalo
            except ValueError:
                print('Entrada inválida. Por favor, digite um número para a nota.')

    alunos.append({'nome': nome, 'idade': idade, 'notas': notas})

#Jhorlen Vulgor Pitch
def listar_alunos():
    if not alunos:
        print("\nNão há alunos cadastrados.")
        return

    for aluno in alunos:
        media = sum(aluno['notas']) / len(aluno['notas'])
        print(f"\nNome: {aluno['nome']}")
        print(f"Idade: {aluno['idade']}")
        print(f"Notas: {aluno['notas']}")
        print(f"Média: {media:.2f}")
        
        situacao = "Aprovado" if media >= 6 else "Reprovado"
        print(f"Aluno -> {situacao}!")


#Paulo Victor Vulgor Paulada
def buscar_aluno_por_nome():
    #Solicita ao usuário que digite parte do nome do aluno e converte o texto para minúsculas
    #Não altera caracteres que já estão em minúsculas. usando lower
    busca_aluno = input('Digite nome que gostaria buscar:').lower()
    
    #contenha o termo digitado pelo usuário
    encontrados = [aluno for aluno in alunos if busca_aluno in aluno['nome'].lower()]

    #Verifica se algum aluno foi encontrado
    if encontrados:
        #Exibe a quantidade de alunos encontrados
        print(f'{len(encontrados)}, aluno(s) encontrado(s):\n')
        
        #Para cada aluno encontrado, chama a função 'exibir_aluno' para mostrar os detalhes
        for aluno in encontrados:
            exibir_aluno(aluno)
    else:
        #Caso  não estive na lista
        print('Nenhum aluno encontrado com esse nome.\n')

def exibir_aluno(aluno):
    media = sum(aluno['notas']) / len(aluno['notas'])
    status = 'Aprovado' if media >= 6 else 'Reprovado'
    print(f"Nome: {aluno['nome']}")
    print(f"Idade: {aluno['idade']}")
    print(f"Notas: {aluno['notas']}")
    print(f"Média: {media:.2f} - {status}")
    print('-' * 30)

#Jhorlen Vulgor Pitch
def mostrar_aprovados():
    print("\nAlunos Aprovados (média >= 6):")
    for aluno in alunos:
        media = sum(aluno['notas']) / len(aluno['notas'])
        if 0 <= media <= 10:
            if media >= 6:
                print(f"\nNome: {aluno['nome']}")
                print(f"Notas: {aluno['notas']}")
                print(f"Média: {media:.2f}")
        else:
            print(f"\nMédia inválida para o aluno {aluno['nome']}")

#Jhorlen Vulgor Pitch
def mostrar_reprovados():
    print("\nAlunos Reprovados (média < 6):")
    for aluno in alunos:
        media = sum(aluno['notas']) / len(aluno['notas'])
        if 0 <= media <= 10:
            if media <= 6:
                print(f"\nNome: {aluno['nome']}")
                print(f"Notas: {aluno['notas']}")
                print(f"Média: {media:.2f}")
        else:
            print(f"\nMédia inválida para o aluno {aluno['nome']}")

#Fernanda Vulgor Monitora
def editar_cadastro():
    """Vai editar os dados de um aluno existente"""
    buscar_aluno_por_nome()
    nome = input("\nDigite o nome completo do aluno que deseja editar: ").strip()
    
    for aluno in alunos:
        if aluno['nome'].lower() == nome.lower():
            print("\nEditando aluno:")
            exibir_aluno(aluno)
            
            #Atualiza nome
            novo_nome = input(f"\nNovo nome ({aluno['nome']}): ").title().strip()
            if novo_nome:
                aluno['nome'] = novo_nome
            
            #Atualiza idade
            nova_idade = input(f"Nova idade ({aluno['idade']}): ").strip()
            if nova_idade.isdigit():
                aluno['idade'] = int(nova_idade)
            
            #Atualiza notas
            for i in range(4):
                while True:
                    try:
                        nova_nota = float(input(f"Nova nota {i+1} ({aluno['notas'][i]}): "))
                        if 0 <= nova_nota <= 10:
                            aluno['notas'][i] = nova_nota
                            break
                        print("Nota deve ser entre 0 e 10!")
                    except:
                        print("Digite um número válido!")
            
            print("\nCadastro atualizado com sucesso!")
            exibir_aluno(aluno)
            return
    
    print("\nAluno não encontrado!")

#Fernanda Vulgor Monitora
def excluir_cadastro():
    """Remove um aluno da lista"""
    nome = input("\nDigite o nome completo do aluno que deseja excluir: ").strip()
    
    for aluno in alunos:
        if aluno['nome'].lower() == nome.lower():
            print("\nAluno encontrado:")
            exibir_aluno(aluno)

            confirmacao = input("\nDeseja mesmo excluir? (s/n): ").lower()
            if confirmacao.startswith('s'):
                alunos.remove(aluno)
                print("Aluno removido!")
            else:
                print("Exclusão cancelada.")
            return  #Sai da função após ação

    print("\nAluno não encontrado!")

def limpar():
    os.system('pause')
    os.system('cls')

def menu():
    opcao = 0
    while opcao != 8:
        print('=====Sistema de Alunos=====')
        print('1. Cadastrar aluno') 
        print('2. Listar alunos')
        print('3. Buscar aluno por nome') 
        print('4. Exibir aprovados')
        print('5. Exibir reprovados') 
        print('6. Editar cadastro')
        print('7. Excluir cadastro')
        print('8. Sair')
        print('===========================')
        
        opcao = int(input("Escolha uma opção: "))

        if opcao == 1:
            print("Você escolheu a opção Cadastrar aluno!")
            cadastrar_aluno()
        elif opcao == 2:
            print("Você escolheu a opção Listar alunos!")
            listar_alunos()
        elif opcao == 3:
            print("Você escolheu a opção Buscar aluno por nome!")
            buscar_aluno_por_nome()
        elif opcao == 4:
            print("Você escolheu a opção Exibir aprovados!")
            mostrar_aprovados()
        elif opcao == 5:
            print("Você escolheu a opção Exibir reprovados!")
            mostrar_reprovados()
        elif opcao == 6:
            print("Você escolheu a opção Editar cadastro!")
            editar_cadastro()
        elif opcao == 7:
            print("Você escolheu a opção Excluir cadastro!")
            excluir_cadastro()
        elif opcao == 8:
            print("Você escolheu a opção!\nSaindo...")
        else:
            print("Opção inválida.")
        limpar()
menu()