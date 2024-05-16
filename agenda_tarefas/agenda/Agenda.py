from agenda.Tarefa import Tarefa
import os


class Agenda:
    def __init__(self):
        self.tarefas = []

    def adicionar_tarefa(self, nova_tarefa):
        self.tarefas.append(nova_tarefa)
        self.salvar_agenda("agenda_tarefas.txt")
        print("Tarefa adicionada com sucesso!")

    def remover_tarefa(self, tarefa):
        if tarefa in self.tarefas:
            self.tarefas.remove(tarefa)
            self.salvar_agenda("agenda_tarefas.txt")  
            print("Tarefa removida com sucesso!")
        else:
            print("Tarefa não encontrada.")


    def exibir_tarefas(self):
        if not self.tarefas:
            print("Nenhuma tarefa na agenda.")
        else:
            print("Tarefas na agenda:\n")
            for tarefa in self.tarefas:
                print(f'Nome: {tarefa.nome}\n Início: {tarefa.data_inicio}\n Término: {tarefa.data_termino}\n Prioridade: {tarefa.prioridade}\n Estado: {tarefa.estado_tarefa}\n')

    def salvar_agenda(self, nome_arquivo):
        try:
            with open(nome_arquivo, 'w') as file:
                for tarefa in self.tarefas:
                    file.write(f"{tarefa.nome}, {tarefa.data_inicio}, {tarefa.data_termino}, {tarefa.prioridade}, {tarefa.estado_tarefa}\n")
        except IOError:
            print("Erro ao salvar a agenda. Verifique se o arquivo e as permissões estão corretos.")

    def carregar_agenda(self, nome_arquivo):
        try:
            # Verifica se o arquivo existe, se não existir, cria um novo
            if not os.path.exists(nome_arquivo):
                with open(nome_arquivo, 'w'):
                    pass  # Cria o arquivo vazio
                    print(f"Arquivo {nome_arquivo} criado.")
            with open(nome_arquivo, 'r') as file:
                for line in file:
                    dados_tarefa = line.strip().split(',')
                    nome, data_inicio, data_termino, prioridade, estado_tarefa = dados_tarefa
                    nova_tarefa = Tarefa(nome, data_inicio, data_termino, prioridade, estado_tarefa)
                    self.adicionar_tarefa(nova_tarefa)
        except Exception as e:
            print("Erro ao carregar a agenda:", e)