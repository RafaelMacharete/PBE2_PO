class Habitat():
    def __init__(self, nome_habitat):
        self.nome_habitat = nome_habitat

class Alimento():
    def __init__(self, nome_alimento):
        self.nome_alimento = nome_alimento

class Animal(Alimento, Habitat):
    def __init__(self, nome_animal, nome_alimento, nome_habitat):
        super().__init__(nome_alimento, nome_habitat)
        self.nome_animal = nome_animal

class Funcionario():
    def __init__(self, nome_):

class Veterinario():