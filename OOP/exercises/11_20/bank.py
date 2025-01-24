class Bank():
    def __init__(self, bank_name):
        self.bank_name = bank_name
        self.customer_registration = []

    def register_customer(self, customer_id, customer_name, customer_balance):
        self.cust_id = customer_id
        
        self.customer_registration.append(
            {'id': customer_id, 
             'name': customer_name,
             'balance': customer_balance
             })

    def action_on_account(self, option_chosen, value, account_transfer_id=None):
        customer = self.customer_registration[self.cust_id]
        
        # Withdrawal
        if option_chosen == 1:
            customer['balance'] -= value
            print(f'o {customer["name"]} agora tem: {customer["balance"]}')
        # Deposit
        elif option_chosen == 2:
            customer['balance'] += value
            print(f'o {customer["name"]} agora tem: {customer["balance"]}')
        # Transfer
        elif option_chosen == 3 and account_transfer_id is not None:
            customer['balance'] -= value
            transfer_customer = self.customer_registration[account_transfer_id]
            transfer_customer['balance'] += value
            print(f'o {customer["name"]} transferiu {value} para: {transfer_customer["name"]}')

# Testando
bank1 = Bank('Bradesco')
bank2 = Bank('Inter')

bank1.register_customer(0, 'Rafael', 10)
bank1.register_customer(1, 'Leafar', 20)

bank2.register_customer(0, 'asd', 30)
bank2.register_customer(1, 'dsa', 40)

# Fazendo uma transferência
bank1.action_on_account(1, 10, 0)
