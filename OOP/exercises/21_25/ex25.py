class Character():
    def __init__(self, hp, strong, defense, hability):
        self.hp = hp
        self.strong = strong
        self.defense = defense
        self.hability = hability

    def Round(self, adversary):
        while self.hp > 0 and adversary.hp > 0:
            print(f'vida do protagonista: {self.hp}\n')
            print(f'vida do vilão: {adversary.hp}\n')

            print('O protagonista usou o ataque',self.hability)
            print(f'E causou: {self.strong} de dano\n')
            adversary.hp -= self.strong

            print('O Vilão usou o ataque',adversary.hability)
            print(f'E causou: {adversary.strong} de dano\n')
            self.hp -= adversary.strong

            if self.hp <= 0 or adversary.hp <= 0:
                if self.hp <= 0:
                    print('O vilão ganhou!')
                else:
                    print('O protagonista ganhou!')

protagonista = Character(100, 20, 15, 'Rasteira')
vilao = Character(85, 27, 17, 'Ataque Rápido')

protagonista.Round(vilao)