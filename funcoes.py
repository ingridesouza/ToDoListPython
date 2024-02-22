def criar_tarefa(nome, descricao, prioridade, categoria, concluida=False):
    return {'Nome_Tarefa': nome,
            'Descricao_Tarefa': descricao,
            'Prioridade_Tarefa': prioridade,
            'Categoria_Tarefa': categoria,
            'Status_Tarefa': concluida}
    
#-----------------------------------------------------------------------
# def adicionar_tarefa(lista_tarefas, tarefas):
#     lista_tarefas.append(tarefas)
#     print('Tarefa Adicionada!')

#-----------------------------------------------------------------------
    
def remover_tarefa(lista_tarefas,nome_tarefa):
    for tarefa in lista_tarefas:
     if tarefa["Nome_tarefa"] == nome_tarefa:
        tarefa.remove(tarefa)
        print(f'Tarefa {nome_tarefa} removida com sucesso.')
        return
    print(f'Tarefa {nome_tarefa} não encontrada na lista.')

#-----------------------------------------------------------------------
# Função para listar tarefas
def listar_tarefas(lista_tarefas):
    # o 'i' é o indice do item
    # para cada tarefa na lista de tarefas, pega cada tarefa e indice da lista de tarefas
    for i, tarefa in enumerate(lista_tarefas, start=1):
        print(f'{i}. {tarefa['Nome_Tarefa']} - Descrição: {tarefa['Descricao_Tarefa']} - Prioridade: {tarefa['Prioridade_Tarefa']} - Categoria: {tarefa['Categoria_Tarefa']} - Concluída: {tarefa['Status_Tarefa']}')
        print('-'*50)

#-----------------------------------------------------------------------
# Função para marcar tarefa como concluída
def marcar_como_concluida(lista_tarefas, nome_tarefa):

    for tarefa in lista_tarefas:
        if tarefa["Nome_Tarefa"] == nome_tarefa:
            # Marca a tarefa como concluída, alterando o valor da chave "Status_Tarefa" para True
            tarefa["Status_Tarefa"] = True
            print(f'Tarefa {nome_tarefa} marcada como concluída!')
            return
    print(f'Tarefa {nome_tarefa} não encontrada.')

#-----------------------------------------------------------------------
# Função para exibir tarefas por prioridade
    
def exibir_por_prioridade(lista_tarefas, prioridade):

    # Cria uma lista de tarefas filtradas pela prioridade
    tarefas_filtradas = [tarefa for tarefa in lista_tarefas if tarefa["Prioridade_Tarefa"] == prioridade]

    if tarefas_filtradas:
        print(f"Tarefas com prioridade {prioridade}:")
        listar_tarefas(tarefas_filtradas)
    else:
        print(f"Nenhuma tarefa encontrada com prioridade {prioridade}.")

#---------------------------------------------------------------------
# Função para exibir tarefas por categoria
        
def exibir_por_categoria(lista_tarefas, categoria):

    tarefas_filtradas = [tarefa for tarefa in lista_tarefas if tarefa["Categoria_Tarefa"] == categoria]

    if tarefas_filtradas:
        print(f"Tarefas na categoria {categoria}:")
        listar_tarefas(tarefas_filtradas)
    else:
        print(f"Nenhuma tarefa encontrada na categoria {categoria}.")

#---------------------------------------------------------------------
#Função para exibir por status 
        
def exibir_por_status(lista_tarefas, status):

    tarefas_filtradas = [tarefa for tarefa in lista_tarefas if tarefa ["Status_Tarefa"] == status]

    if tarefas_filtradas:
        print(f'Tarefas no status {status}:')
        lista_tarefas(tarefas_filtradas)
    else:
        print(f'Nenhuma tarefa encontrada no status {status}.')
