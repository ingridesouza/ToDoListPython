import funcoes 
from lista import lista_tarefas

controleLoop = True

while controleLoop:
    print('''
          1- Inserir uma tarefa
          2- Visualizar Tarefas
          3- Marcar como concluida
          4- Remover Tarefa
          5- Exibir Tarefas por prioridade ou status
          6 - Para Encerrar
          ''')
    escolha = input("Escolha uma das opções: ")

    match escolha:
        case '1':
            nome = input("Digite o nome da tarefa: ")
            descricao = input("Digite a descrição da tarefa: ")
            prioridade = input("Digite a prioridade da tarefa: ")
            categoria = input("Digite a categoria da tarefa: ")
            nova_tarefa = funcoes.criar_tarefa(nome, descricao, prioridade, categoria)
            lista_tarefas.append(nova_tarefa)
            print("Tarefa inserida com sucesso!")
            
        case '2':
            funcoes.listar_tarefas(lista_tarefas)
        
        case '3':
            tarefa = input('Digite o nome da tarefa que deseja marcar como concluida: ')
            funcoes.marcar_como_concluida(lista_tarefas, tarefa)

        case '4':
            nomeTarefaRemover = input('Digite o nome da tarefa que deseja remover:')
        
        case '5':
            print('-----FILTRO DE TAREFAS-----')
            filtroEscolha = input('Escolha uma opção:\n\n'
                      '1- Filtrar a tarefa por categoria\n'
                      '2- Filtrar tarefa por prioridade\n'
                      '3- Filtrar tarefa por status\n')
            match filtroEscolha:
                case '1':
                    categoriaFiltro = input('Digite a categoria da tarefa: ')
                    funcoes.exibir_por_categoria(lista_tarefas, categoriaFiltro)
                case '2':
                    prioridadeFiltro = input('Digite a prioridade ou status da tarefa: ')
                    funcoes.exibir_por_prioridade(lista_tarefas, prioridadeFiltro)
                case '3':
                    statusFiltro = input('Digite o status da tarefa: ')
                    funcoes.exibir_por_status(lista_tarefas, statusFiltro)
                case _:
                    print("Opção inválida! Por favor, escolha uma opção válida.")

        case '6':
            print("Encerrando o programa. Até Logo!")
            controleLoop = False #faz com que o loop while seja interrompido e o programa saia do loop, encerrando a execução.
            break

            # controleLoop = Quando é True, o programa continua em execução; quando é False, o programa termina. Isso é uma forma comum de implementar a lógica de menu em programas que precisam de um loop contínuo até que o usuário decida sair.
        case _ :
            print('Opção Inválida. Tente Novamente.')

        
