class VendingMachine():
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

    def buy_product(self, prod_choice, money_value, ):
        for product in self.products_list:
            if product['id'] == prod_choice:  # Verifica se o ID corresponde
                if money_value >= product['price']:  # Verifica se o dinheiro é suficiente
                    change = money_value - product['price']
                    print(f"You bought one {product['name']} for {product['price']}.")
                    print(f"Your change is: {change}")
                    return
                else:
                    print("Insufficient funds.")
                    return    
    
    def show_stock(self):
        if not self.products_list:
            print("The vending machine is empty.")
        else:
            print(f"Products in {self.store_name}:")
            for product in self.products_list:
                print(f"ID: {product['id']}, Name: {product['name']}, Price: {product['price']}")


vending_machine1 = VendingMachine('Maquina 1')

vending_machine1.show_stock()
    
vending_machine1 = VendingMachine('Machine 1')

vending_machine1.register_products('Soda', 2.5)
vending_machine1.register_products('Chips', 3.0)
vending_machine1.register_products('Candy', 1.5)

vending_machine1.show_stock()

vending_machine1.buy_product(1, 5.0)