import funcoes 
from bancoDados import lista

controleLoop = True

while controleLoop:
    print('''
          1- Inserir uma tarefa
          2- Visualizar Tarefas
          3- Marcar como concluida
          4- Exibir Tarefas por prioridade ou status
          5 - Para encerrar
          ''')
    escolha = input("Escolha uma das opções: ")

    match escolha:
        case "1":
            nome = input("Digite o nome da tarefa ")
            descricao = input("Digite a descricao da tarefa ")
            prioridade = input("Digite a prioridade da tarefa ")
            status = input("Digite o status da tarefa ")
            categoria = input("Digite a categoria da tarefa ")
            funcoes.inserirTarefa(lista, nome, descricao, prioridade, categoria, status)
            
        case "2":
            for listar in lista:
                print(listar)
        
            
        case "5":
            print("Saindo...")
            break
