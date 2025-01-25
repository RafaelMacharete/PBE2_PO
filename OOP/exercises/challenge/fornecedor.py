class Fornecedor:
    def __init__(self, nome, tipo_servico, contato):
        self.nome = nome
        self.tipo_servico = tipo_servico
        self.contato = contato

    def __str__(self):
        return f"{self.nome} ({self.tipo_servico}) - Contato: {self.contato}"