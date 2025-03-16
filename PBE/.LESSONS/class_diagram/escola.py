import time
from colorama import Fore

class Escola():
    def __init__(self, nome_escola):
        self.nome_escola = nome_escola
        self.lista_dados = []
        self.historico = []
        
    def registrar_historico(self, acao):
        horario = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        self.historico.append(f"[{horario}] {acao}")

class Diretoria(Escola):
    def __init__(self, nome_escola):
        super().__init__(nome_escola)

    def cadastrar_funcionario(self, funcionario):
        self.lista_dados.append(funcionario)
        self.registrar_historico(f"Funcionário {funcionario} cadastrado.")
        print(f"Funcionário {funcionario} cadastrado!")

    def atualizar_funcionario(self):
        self.registrar_historico("Funcionário atualizado.")
        print("Funcionário Atualizado")

    def deletar_funcionario(self, funcionario):
        if funcionario in self.lista_dados:
            self.lista_dados.remove(funcionario)
            self.registrar_historico(f"Funcionário {funcionario} deletado.")
            print(f"Funcionários atuais:\n {self.lista_dados}")
        else:
            print("Funcionário não encontrado.")

    def exibir_historico(self):
        print("Histórico de ações:")
        for evento in self.historico:
            print(evento)

class Aluno():
    def __init__(self, ra, nome, turma):    
        self.ra = ra
        self.nome = nome
        self.turma = turma
    
class Professor():
    def __init__(self, nif, nome, salario):
        self.nif = nif
        self.nome = nome
        self.salario = salario
    
escola1 = Escola("Senai")

diretoria1 = Diretoria("OPP")

funcionario1 = Professor(34, "Marcia", 16000)
funcionario2 = Professor(40, "Israel Gomes", 25000)
funcionario3 = Professor(36, "Dorival", -20000)

while True:
    opcao = int(input(f"O que você deseja fazer?\n{Fore.LIGHTYELLOW_EX}[0] - Sair{Fore.RESET}\n{Fore.LIGHTGREEN_EX}[1] - Cadastrar{Fore.RESET}\n{Fore.LIGHTBLUE_EX}[2] - Atualizar{Fore.RESET}\n{Fore.LIGHTRED_EX}[3] - Deletar{Fore.RESET}\n{Fore.LIGHTMAGENTA_EX}[4] - Exibir Histórico{Fore.RESET}\n"))
    
    if opcao == 0:
        break
    elif opcao == 1:
        diretoria1.cadastrar_funcionario(funcionario1.nome)
        diretoria1.cadastrar_funcionario(funcionario2.nome)
        diretoria1.cadastrar_funcionario(funcionario3.nome)
    elif opcao == 2:
        diretoria1.atualizar_funcionario()
    elif opcao == 3:
        nome = input('Digite o nome do funcionário: ')
        diretoria1.deletar_funcionario(nome)
    elif opcao == 4:
        diretoria1.exibir_historico()