import os
from agenda.Tarefa import Tarefa


class Agenda:
    def __init__(self):
        self.tarefas = [] # Inicializa a lista de tarefas

    def adicionar_tarefa(self, nova_tarefa, show_message=True):
        self.tarefas.append(nova_tarefa) # Adiciona a nova tarefa à lista
        self.salvar_agenda("agenda_tarefas.txt") # Salva a agenda no arquivo
        if show_message:
            print("Tarefa adicionada com sucesso!")

    def remover_tarefa(self, tarefa):
        if tarefa in self.tarefas:
            self.tarefas.remove(tarefa) # Remove a tarefa da lista
            self.salvar_agenda("agenda_tarefas.txt") # Salva a agenda atualizada no arquivo
            print("\nTarefa removida com sucesso!")
        else:
            print("Tarefa não encontrada.")

    def exibir_tarefas(self):
        if not self.tarefas:
            print("\nNenhuma tarefa na agenda.")
        else:
            print("Tarefas na agenda:\n")
            for tarefa in self.tarefas:
                print(f'Nome: {tarefa.nome}\nInício: {tarefa.data_inicio}\nTérmino: {tarefa.data_termino}\nPrioridade: {tarefa.prioridade}\nEstado: {tarefa.estado_tarefa}\n')

    def salvar_agenda(self, nome_arquivo):
        try:
             # Escreve tarefa por tarefa no arquivo
            with open(nome_arquivo, 'w') as file:
                file.write("[Nome da tarefa, Data de Inicio da tarefa, Data de Termino da tarefa, Prioridade, Estado]\n\n")
                for tarefa in self.tarefas:
                    file.write(f"{tarefa.nome}, {tarefa.data_inicio}, {tarefa.data_termino}, {tarefa.prioridade}, {tarefa.estado_tarefa}\n")
        except IOError:
            print("Erro ao salvar a agenda. Verifique se o arquivo e as permissões estão corretos.")

    def carregar_agenda(self, nome_arquivo):
        try:
             # Cria o arquivo se ele não existir
            if not os.path.exists(nome_arquivo):
                with open(nome_arquivo, 'w'):
                    pass
                print(f"Arquivo {nome_arquivo} criado.")
            with open(nome_arquivo, 'r') as file:
                next(file)
                next(file)
                for line in file:
                    dados_tarefa = line.strip().split(', ')
                    nome, data_inicio, data_termino, prioridade, estado_tarefa = dados_tarefa
                    # Cria uma nova tarefa a partir dos dados do arquivo
                    nova_tarefa = Tarefa(nome, data_inicio, data_termino, prioridade, estado_tarefa)
                    self.adicionar_tarefa(nova_tarefa, show_message=False) # Adiciona a nova tarefa à lista de tarefas
        except Exception as e:
            print("Erro ao carregar a agenda:", e)
