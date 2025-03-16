class Pagamento:
    def __init__(self, parcela, valor_total, data_vencimento):
        self.parcela = parcela
        self.valor_total = valor_total
        self.data_vencimento = data_vencimento
        self.status = "Pendente"

    def atualizar_status(self, status):
        self.status = status

    def __str__(self):
        return f"Parcela {self.parcela} - Valor: {self.valor_total} - Vencimento: {self.data_vencimento} - Status: {self.status}"
