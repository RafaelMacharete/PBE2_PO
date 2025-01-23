class Employee():
    def __init__(self, employee_name, employee_salary, employee_position):
        self.name = employee_name
        self.salary = employee_salary
        self.emp_position = employee_position

    def calc_net_salary(self, tax_pct, benefits):
        self.net_salary = tax_pct * 100 * self.salary - benefits
#