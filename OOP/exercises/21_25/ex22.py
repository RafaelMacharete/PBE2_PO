class Categoria():
    def __init__(self, category_name):
        self.cat_name = category_name

class Produto(Categoria):
    def __init__(self, product_name, category_name):
        super().__init__(category_name)
        self.prod_name = product_name

class Fornecedor(Produto):
    def __init__(self, product_name, category_name):
        super().__init__(product_name, category_name)
        self.prod