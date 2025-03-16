class VirtualStore():
    def __init__(self, store_name):
        self.store_name = store_name
        self.products_list = []
        
    def register_products(self, name_prod, price_prod):
        id_prod = len(self.products_list)

        self.product_data = {
            'id': id_prod,
            'name': name_prod,
            'price': price_prod
        }
        
        self.products_list.append(self.product_data)

    def shop_cart(self, prod_choice, prod_amount, discount = 0):
        self.data_cart = self.product_data
        self.total_value = self.products_list[prod_choice]['price'] * prod_amount - discount
        
        self.data_cart.pop('id')
        self.data_cart.update({'amount': prod_amount, 'total value': self.total_value})

        return self.data_cart
        

virtual_store1 = VirtualStore('Redragon')

virtual_store1.register_products('Teclado', 20)
virtual_store1.register_products('Mouse', 10)

print(virtual_store1.shop_cart(1, 10, 10))