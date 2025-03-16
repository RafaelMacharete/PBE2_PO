class Produto:
    def __init__(self, nome_produto, preco):
        self.nome = nome_produto
        self.preco = preco

    def __str__(self):
        return f"{self.nome} - R${self.preco:.2f}"


class Cliente:
    def __init__(self, nome_cliente):
        self.nome = nome_cliente
        self.historico_cliente = []

    def adicionar_historico(self, pedido):
        self.historico_cliente.append(pedido)

    def exibir_historico(self):
        print("\nHistórico de Compras:")
        if not self.historico_cliente:
            print("Nenhuma compra realizada.")
        else:
            for i, pedido in enumerate(self.historico_cliente, 1):
                print(f"Pedido {i}: {pedido}")

    def __str__(self):
        return f"Cliente: {self.nome}"


class Pedido:
    def __init__(self, cliente):
        self.cliente = cliente
        self.produtos = []
        self.valor_total = 0

    def adicionar_produto(self, produto):
        self.produtos.append(produto)
        self.valor_total += produto.preco

    def aplicar_desconto(self, percentual):
        desconto = self.valor_total * (percentual / 100)
        self.valor_total -= desconto
        print(f"Desconto de {percentual}% aplicado. Total com desconto: R${self.valor_total:.2f}")

    def calcular_frete(self, distancia_km):
        frete = 5 + 0.5 * distancia_km
        self.valor_total += frete
        print(f"Frete: R${frete:.2f}. Total com frete: R${self.valor_total:.2f}")

    def finalizar(self):
        self.cliente.adicionar_historico(self)
        print(f"Pedido finalizado! Total: R${self.valor_total:.2f}")

    def __str__(self):
        produtos_listados = ", ".join([produto.nome for produto in self.produtos])
        return f"Produtos: {produtos_listados} | Total: R${self.valor_total:.2f}"


produto1 = Produto("item", 100)
produto2 = Produto("item1", 20)
produto3 = Produto("algo", 30)

cliente = Cliente("Rafael")

pedido = Pedido(cliente)

pedido.adicionar_produto(produto1)
pedido.adicionar_produto(produto2)

pedido.aplicar_desconto(10)

pedido.calcular_frete(20)

pedido.finalizar()

cliente.exibir_historico()
