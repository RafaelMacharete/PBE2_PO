class BankAccount():
# def __eq__, __le__, __ge__, gt, lt
    def __init__(self, id, account_holder, holder_balance):
        self.id = id
        self.account_holder = account_holder
        self.holder_balance = holder_balance

    def bank_deposit(self, deposit_value):
        self.holder_balance += deposit_value
        return deposit_value
        
    def bank_withdrawal(self, withdrawal_value):
        self.holder_balance -= withdrawal_value
        return withdrawal_value

    def __str__(self):
        return f'Currente balance = {self.holder_balance}'
    


bank_account1 = BankAccount(0, 'Rafael', 1234.56)
bank_account2 = BankAccount(1, 'Leafar', 1234.56)

bank_account1.bank_deposit(123)
bank_account2.bank_withdrawal(321)
print(f'A value of {bank_account1.bank_deposit(100)} was deposited into the id:{bank_account1.id} account\n{bank_account1}')
print(f'A value of {bank_account2.bank_withdrawal(321)} was withdrawn from the id:{bank_account2.id} account\n{bank_account2}')