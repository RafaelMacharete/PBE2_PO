import calendar
from datetime import date, timedelta

class Calendario:
    def __init__(self):
        self.feriados = {
            date(2025, 1, 1): "Ano Novo",
            date(2025, 12, 25): "Natal",
            date(2025, 9, 7): "Independência do Brasil",
            date(2025, 11, 15): "Proclamação da República"
        }

    def exibir_mes(self, ano, mes):
        print(calendar.TextCalendar().formatmonth(ano, mes))

    def verificar_feriado(self, dia, mes, ano):
        data = date(ano, mes, dia)
        if data in self.feriados:
            return f"{data.strftime('%d/%m/%Y')} é feriado: {self.feriados[data]}"
        return f"{data.strftime('%d/%m/%Y')} não é um feriado."

    def diferenca_dias(self, dia1, mes1, ano1, dia2, mes2, ano2):
        data1 = date(ano1, mes1, dia1)
        data2 = date(ano2, mes2, dia2)
        diferenca = abs((data2 - data1).days)
        return f"A diferença entre {data1.strftime('%d/%m/%Y')} e {data2.strftime('%d/%m/%Y')} é de {diferenca} dias."


calendario = Calendario()

print("Calendário de Março/2025:")
calendario.exibir_mes(2025, 3)

print(calendario.verificar_feriado(25, 12, 2025))
print(calendario.verificar_feriado(10, 10, 2025))

print(calendario.diferenca_dias(1, 1, 2025, 25, 12, 2025))
