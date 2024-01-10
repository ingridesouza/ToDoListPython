# Insere a tarefa na lista
def inserir_tarefa(BD:list, nome:str, descricao:str, prioridade:int, categoria:str, status:bool = False):
  BD.append({'Nome_Tarefa':nome, 'Descricao_Tarefa': descricao, 'Prioridade_Tarefa': prioridade, 'Status_tarefa': status, 'Categoria_Tarefa': categoria })  
  return BD

# Remove a tarefa da lista
def remover_tarefa(BD:list, nome:str):
  contador = 0  
  
  for contador in BD.count:
    if BD[contador]["Nome_Tarefa"] == nome:
      BD.pop[contador]
      

# Marca a tarefa como concluída
def concluir_tarefa(BD:list, nome:str):
  contador = 0  
  
  for contador in BD.count:
    if BD[contador]["Nome_Tarefa"] == nome:
      BD[contador]["Status_Tarefa"] = True
