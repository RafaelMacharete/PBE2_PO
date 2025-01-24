class Product():
    def __init__(self, product_name, product_price, qnt_in_stock):
        self.name = product_name
        self.prod_price = product_price
        self.stock = qnt_in_stock

    def calc_total_value(self):
        if self.stock > 0:
            self.total_value = self.prod_price * self.stock
            return self.total_value
        return 'Stock is empty'
    
product1 = Product('Biscoito', 5, 0)

total_value = product1.calc_total_value()

print(f'Total product {product1.name} value: {total_value}')