from evento import Evento

class Casamento(Evento):
    def __init__(self, data, hora, local, descricao, noivos):
        super().__init__(data, hora, local, descricao, "Casamento")
        self.noivos = noivos

class EventoCorporativo(Evento):
    def __init__(self, data, hora, local, descricao, empresa):
        super().__init__(data, hora, local, descricao, "Evento Corporativo")
        self.empresa = empresa

class Festa(Evento):
    def __init__(self, data, hora, local, descricao, tema):
        super().__init__(data, hora, local, descricao, "Festa")
        self.tema = tema