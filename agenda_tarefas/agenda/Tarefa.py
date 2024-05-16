class Tarefa:
    def __init__(self, nome, data_inicio, data_termino, prioridade, estado_tarefa='Pendente'):
        self._nome = nome
        self._data_inicio = data_inicio
        self._data_termino = data_termino
        self._prioridade = prioridade
        self._estado_tarefa = estado_tarefa
        
    @property
    def nome(self):
        return self._nome
    
    @nome.setter
    def nome(self, nome):
        self._nome = nome

    @property
    def data_inicio(self):
        return self._data_inicio
    
    @data_inicio.setter
    def data_inicio(self, data_inicio):
        self._data_inicio = data_inicio

    @property
    def data_termino(self):
        return self._data_termino
    
    @data_termino.setter
    def data_termino(self, data_termino):
        self._data_termino = data_termino
        
    @property
    def prioridade(self):
        return self._prioridade
    
    @prioridade.setter
    def prioridade(self, prioridade):
        self._prioridade = prioridade
    
    @property
    def estado_tarefa(self):
        return self._estado_tarefa
    
    @estado_tarefa.setter
    def estado_tarefa(self, estado_tarefa):
        self._estado_tarefa = estado_tarefa
