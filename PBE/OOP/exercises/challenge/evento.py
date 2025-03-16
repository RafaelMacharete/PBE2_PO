class Evento:
    def __init__(self, data, hora, local, descricao, tipo):
        self.data = data
        self.hora = hora
        self.local = local
        self.descricao = descricao
        self.tipo = tipo
        self.tarefas = []
        self.fornecedores = []
        self.pagamentos = []

    def adicionar_tarefa(self, tarefa):
        self.tarefas.append(tarefa)

    def adicionar_fornecedor(self, fornecedor):
        self.fornecedores.append(fornecedor)

    def adicionar_pagamento(self, pagamento):
        self.pagamentos.append(pagamento)

    def __str__(self):
        return f"{self.tipo} - {self.descricao} em {self.local} no dia {self.data}"