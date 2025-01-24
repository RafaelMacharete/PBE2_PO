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

    def shop_cart(self, prod_choice, prod_amount):
        self.total_value = self.products_list[prod_choice]
        

virtual_store1 = VirtualStore('Redragon')

virtual_store1.register_products('Teclado', 2)
virtual_store1.register_products('Mouse', 1)

virtual_store1.shop_cart(1,2)