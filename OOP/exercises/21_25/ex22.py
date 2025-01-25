class Categoria:
    def __init__(self, nome):
        self.nome = nome

class Produto:
    def __init__(self, nome, categoria, preco_compra, preco_venda, estoque=0):
        self.nome = nome
        self.categoria = categoria
        self.preco_compra = preco_compra
        self.preco_venda = preco_venda
        self.estoque = estoque

    def adicionar_estoque(self, quantidade):
        self.estoque += quantidade

    def remover_estoque(self, quantidade):
        if quantidade <= self.estoque:
            self.estoque -= quantidade
        else:
            raise ValueError("Quantidade insuficiente no estoque!")

    def __str__(self):
        return (f"Produto: {self.nome}, Categoria: {self.categoria.nome}, "
                f"Estoque: {self.estoque}, Preço de Venda: R${self.preco_venda:.2f}")

class Fornecedor:
    def __init__(self, nome):
        self.nome = nome

    def fornecer_produto(self, produto, quantidade):
        produto.adicionar_estoque(quantidade)
        print(f"{quantidade} unidades do produto '{produto.nome}' fornecidas por {self.nome}.")

class Compra:
    def __init__(self, produto, quantidade):
        self.produto = produto
        self.quantidade = quantidade

    def registrar_compra(self):
        self.produto.adicionar_estoque(self.quantidade)
        print(f"Compra registrada: {self.quantidade} unidades de '{self.produto.nome}' adicionadas ao estoque.")

class Venda:
    def __init__(self, produto, quantidade):
        self.produto = produto
        self.quantidade = quantidade

    def registrar_venda(self):
        try:
            self.produto.remover_estoque(self.quantidade)
            receita = self.quantidade * self.produto.preco_venda
            print(f"Venda registrada: {self.quantidade} unidades de '{self.produto.nome}' vendidas.")
            print(f"Receita da venda: R${receita:.2f}")
        except ValueError as e:
            print(e)

class Estoque:
    def __init__(self):
        self.produtos = []

    def adicionar_produto(self, produto):
        self.produtos.append(produto)

    def relatorio_inventario(self):
        print("\nRelatório de Inventário:")
        for produto in self.produtos:
            print(produto)


cat_alimentos = Categoria("Alimentos")
cat_eletronicos = Categoria("Eletrônicos")

arroz = Produto("Arroz", cat_alimentos, 5.00, 7.00, 100)
celular = Produto("Celular", cat_eletronicos, 800.00, 1200.00, 50)

fornecedor_joao = Fornecedor("João Fornecimentos")

estoque = Estoque()
estoque.adicionar_produto(arroz)
estoque.adicionar_produto(celular)

fornecedor_joao.fornecer_produto(arroz, 50)

compra = Compra(celular, 20)
compra.registrar_compra()

venda = Venda(arroz, 30)
venda.registrar_venda()

estoque.relatorio_inventario()
