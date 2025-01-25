class Tarefa:
    def __init__(self, descricao, responsavel, prazo):
        self.descricao = descricao
        self.responsavel = responsavel
        self.prazo = prazo
        self.status = "Pendente"

    def atualizar_status(self, status):
        self.status = status

    def __str__(self):
        return f"{self.descricao} - {self.status} (Prazo: {self.prazo})"