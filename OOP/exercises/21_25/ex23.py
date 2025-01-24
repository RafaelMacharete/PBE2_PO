class ToDoList:
    def __init__(self):
        self.lista_tarefas = []
    
    def __str__(self):
        # Exibe a lista de tarefas de forma organizada
        if not self.lista_tarefas:
            return "A lista de tarefas está vazia."
        tarefas = "\n".join(
            [f"ID: {tarefa['id']}, Nome: {tarefa['nome']}, Prioridade: {tarefa['prioridade']}, "
             f"Data de vencimento: {tarefa['data de vencimento']}, Status: {tarefa['status']}"
             for tarefa in self.lista_tarefas]
        )
        return f"Lista de Tarefas:\n{tarefas}"
    
    def criar_tarefa(self, nome, prioridade, data_vencimento, status):
        # Cria uma nova tarefa e adiciona à lista
        id = len(self.lista_tarefas) + 1
        tarefa = {
            'id': id,
            'nome': nome,
            'prioridade': prioridade,
            'data de vencimento': data_vencimento,
            'status': status
        }

        self.lista_tarefas.append(tarefa)
        print("\nTarefa criada com sucesso!")
        print(self)
    
    def editar_tarefa(self, idx, nova_prioridade=None, novo_status=None):
        # Edita uma tarefa com base no ID fornecido
        for tarefa in self.lista_tarefas:
            if tarefa['id'] == idx:  
                if nova_prioridade is not None:
                    tarefa['prioridade'] = nova_prioridade
                if novo_status is not None:
                    tarefa['status'] = novo_status
                
                print("\nTarefa atualizada com sucesso!")
                print(self)
                return
        
        print(f"\nTarefa com ID {idx} não encontrada.")

    def deletar_tarefa(self, nome_tarefa):
        # Remove uma tarefa com base no nome fornecido
        for tarefa in self.lista_tarefas:
            if tarefa['nome'] == nome_tarefa:
                self.lista_tarefas.remove(tarefa)
                print("\nTarefa deletada com sucesso!")
                print(self)
                return
        
        print(f"\nTarefa com nome '{nome_tarefa}' não encontrada.")

    def filtrar_tarefa(self, prioridade):
        # Filtra tarefas com base na prioridade fornecida
        tarefas_filtradas = [
            tarefa for tarefa in self.lista_tarefas if tarefa['prioridade'] == prioridade
        ]
        
        print(f"\nTarefas com prioridade {prioridade}:")
        if not tarefas_filtradas:
            print("Nenhuma tarefa encontrada.")
        else:
            for tarefa in tarefas_filtradas:
                print(f"ID: {tarefa['id']}, Nome: {tarefa['nome']}, Prioridade: {tarefa['prioridade']}, "
                      f"Data de vencimento: {tarefa['data de vencimento']}, Status: {tarefa['status']}")


to_do_list = ToDoList()

to_do_list.criar_tarefa('Trabalhar', 3, 'amanhã', 'em andamento')
to_do_list.criar_tarefa('Estudar', 2, 'hoje', 'pendente')

to_do_list.editar_tarefa(1, nova_prioridade=1, novo_status='finalizado')

to_do_list.deletar_tarefa('Trabalhar')
to_do_list.deletar_tarefa('Correr') 

to_do_list.filtrar_tarefa(2)
