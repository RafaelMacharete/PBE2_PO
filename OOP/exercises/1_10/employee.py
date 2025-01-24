class Employee():
    def __init__(self, employee_name, employee_salary, employee_position):
        self.name = employee_name
        self.salary = employee_salary
        self.emp_position = employee_position

    def calc_net_salary(self, tax_pct, benefits):
        self.net_salary = self.salary - (self.salary * tax_pct / 100) + benefits
        return self.net_salary

    
employee1 = Employee('Rafael', 100, 'Apprentice')

net_salary = employee1.calc_net_salary(10, 20)
print(f"Salário Líquido: {net_salary}")