import calendar
from datetime import date, datetime

class Calendario():
    def __init__(self, ano, mes):
        self.ano = ano
        self.mes = mes
        self.feriados = ['01-01-2025', '18-12-2025']

    def mostar_data(self):
        print(calendar.month(self.ano, self.mes))

    def verificar_feriado(self, data):
        if data in self.feriados:
            print(f'Data {data} é feriado!')
        else: 
            print(f"Data {data} não é feriado!")

    def calcular_datas(self, data1, data2):
        data1 = datetime.strptime(data1, '%d-%m-%Y')
        data2 = datetime.strptime(data2, '%d-%m-%Y')

        data_calculada = abs((data2 - data1).days)
        print(f'A diferença entre {data2.strftime("%d-%m-%Y")} e {data1.strftime("%d-%m-%Y")} é de {data_calculada} dias.')


calendario1 = Calendario(2025, 12)

calendario1.mostar_data()

calendario1.verificar_feriado('18-1-2025')

calendario1.calcular_datas('01-12-2025', '12-12-2025')