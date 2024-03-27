import os
import redis

class TaskManager:
    def __init__(self, host, port, password):
        self.redis_client = redis.StrictRedis(host=host, port=port, password=password)
 
    def adicionar_tarefa(self, descricao, status='EM ANDAMENTO'):
        task_id = str(self.redis_client.incr('contador_tarefas'))
        self.redis_client.hset('tarefas', task_id, descricao)
        self.redis_client.hset('status', task_id, status)
        print(f"Tarefa adicionada. ID: {task_id}")
        input("Pressione Enter para retornar ao menu...")
        return task_id
 
    def listar_tarefas(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        tarefas = self.redis_client.hgetall('tarefas')
        status_tarefas = self.redis_client.hgetall('status')
        print("Lista de Tarefas:")
        for id, descricao in tarefas.items():
            status = status_tarefas.get(id, 'EM ANDAMENTO')
            print(f"Tarefa {id}: {descricao} - Status: {status}")
        input("Pressione Enter para retornar ao menu...")
 
    def marcar_como_concluida(self, id):
        if self.redis_client.hexists('tarefas', id):
            self.redis_client.hset('status', id, 'CONCLUIDA')
            print("Tarefa marcada como concluída!")
        else:
            print("ID de tarefa inválido.")
        input("Pressione Enter para retornar ao menu...")
 
    def remover_tarefa(self, id):
        if self.redis_client.hexists('tarefas', id):
            self.redis_client.hdel('tarefas', id)
            self.redis_client.hdel('status', id)
            print(f"Tarefa {id} removida!")
        else:
            print("ID de tarefa inválido.")
        input("Pressione Enter para retornar ao menu...")
 
    def remover_todas_tarefas(self):
        self.redis_client.delete('tarefas')
        self.redis_client.delete('status')
        self.redis_client.delete('contador_tarefas')
        print("Todas as tarefas foram removidas!")
        input("Pressione Enter para retornar ao menu!")
 
if __name__ == "__main__":
    task_manager = TaskManager(host='redis-17054.c11.us-east-1-3.ec2.cloud.redislabs.com', port=17054, password='8080')
 
    while True:
        os.system('cls' if os.name == 'nt' else 'clear') 
        print("\n1. Adicionar Tarefa")
        print("2. Listar Tarefas")
        print("3. Marcar Tarefa como Concluída")
        print("4. Remover Tarefa")
        print("5. Remover Todas as Tarefas")
        print("6. Sair")
 
        escolha = input("\nEscolha uma opção: ")
 
        if escolha == "1":
            descricao = input("Digite a descrição da tarefa: ")
            task_id = task_manager.adicionar_tarefa(descricao)
        elif escolha == "2":
            task_manager.listar_tarefas()
        elif escolha == "3":
            id = input("Digite o ID da tarefa a ser marcada como concluída: ")
            task_manager.marcar_como_concluida(id)
        elif escolha == "4":
            id = input("Digite o ID da tarefa a ser removida: ")
            task_manager.remover_tarefa(id)
        elif escolha == "5":
            confirmacao = input("Tem certeza que deseja remover todas as tarefas? (s/n): ")
            if confirmacao.lower() == 's':
                task_manager.remover_todas_tarefas()
        elif escolha == "6":
            print("Fim de operação!")
            break
        else:
            print("Opção inválida! Por favor, escolha uma opção válida.")
