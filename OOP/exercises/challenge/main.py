from tarefa import Tarefa
from fornecedor import Fornecedor
from pagamento import Pagamento
from subclasses import Casamento

def gerar_relatorio(eventos, filtro=None):
    for evento in eventos:
        if not filtro or filtro(evento):
            print(evento)
            print("Tarefas:")
            for tarefa in evento.tarefas:
                print(f"  - {tarefa}")
            print("Fornecedores:")
            for fornecedor in evento.fornecedores:
                print(f"  - {fornecedor}")
            print("Pagamentos:")
            for pagamento in evento.pagamentos:
                print(f"  - {pagamento}")
            print("-" * 40)

casamento = Casamento("2025-05-15", "16:00", "Praia", "Cerimônia dos sonhos", ["Alice", "Bob"])
tarefa1 = Tarefa("Contratar buffet", "Alice", "amanha")
tarefa2 = Tarefa("Reservar local", "Bob", "amanha")
fornecedor1 = Fornecedor("Catering Gourmet", "Buffet", "1234-5678")
pagamento1 = Pagamento(1, 1, "ontem")

casamento.adicionar_tarefa(tarefa1)
casamento.adicionar_tarefa(tarefa2)
casamento.adicionar_fornecedor(fornecedor1)
casamento.adicionar_pagamento(pagamento1)

eventos = [casamento]

print("Relatório de eventos:")
gerar_relatorio(eventos)
