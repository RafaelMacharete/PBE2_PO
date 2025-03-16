class Habitat:
    def __init__(self, nome_habitat):
        self.nome_habitat = nome_habitat

class Alimento:
    def __init__(self, nome_alimento):
        self.nome_alimento = nome_alimento

class Animal:
    def __init__(self, nome_animal, fome, saude, nome_alimento, nome_habitat):
        self.nome_animal = nome_animal
        self.fome = fome
        self.saude = saude
        self.alimento = Alimento(nome_alimento)
        self.habitat = Habitat(nome_habitat)

    def __str__(self):
        return f"Animal: {self.nome_animal}, Fome: {self.fome}, Alimento: {self.alimento.nome_alimento}, Habitat: {self.habitat.nome_habitat}"

class Funcionario:
    def __init__(self, nome_funcionario):
        self.nome = nome_funcionario

    def alimentar_animal(self, animal):
        if animal.fome > 0:
            animal.fome -= 1
            print(f"{self.nome} alimentou {animal.nome_animal}. Fome atual: {animal.fome}")
        else:
            print(f"\n{animal.nome_animal} não está com fome.")

    def cuidar_animal(self, animal):
        if animal.saude < 0:
            animal.saude += 1
            print(f'\n{self.nome} alimentou {animal.nome_animal}. Fome atual: {animal.fome}')
        else:
            print(f'\n{animal.nome_animal} não está com fome.')

    
animal1 = Animal('Leão', 1, 2, "Carne", "Savanna")
funcionario1 = Funcionario("João")
funcionario2 = Funcionario("Thiago")

print(animal1)
funcionario1.alimentar_animal(animal1)
funcionario2.alimentar_animal(animal1)

print(animal1)
