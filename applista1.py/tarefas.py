import os
os.system('cls')

lista_tarefas = []

def criar_tarefa(nome_tarefa):
    tarefa = {'nome': nome_tarefa, 'concluída': False}
    lista_tarefas.append(tarefa)
    print(f'Tarefa {tarefa} foi adicionada com sucesso')

def listar_tarefa():
    contador = 1
    for tarefa in lista_tarefas:
        if tarefa['concluída'] == True:
            status = 'Concluída'
        else:
            status = 'Pendente'

        print(str(contador) + '.' + tarefa["nome"] + '[' + status + ']')
        contador += 1
    
def atualizar_tarefa(indice_usuario):
    indice_real = indice_usuario - 1
    lista_tarefas[indice_real]['concluída'] = True
    print('Tarefa atualizada como "concluída"')

def apagar_tarefa(indice_usuario):
    indice_real = indice_usuario - 1

    lista_tarefas.pop(indice_real)