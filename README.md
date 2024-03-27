# Gerenciador de Tarefas usando Redis

Este projeto implementa um simples Gerenciador de Tarefas usando Python e Redis. O Gerenciador de Tarefas permite que os usuários adicionem, listem, marquem tarefas como concluídas, removam tarefas e removam todas as tarefas.

## Redis

Redis é um armazenamento de estrutura de dados em memória de código aberto, usado como banco de dados  NoSQL orientado a  Chave-Valor. Ele suporta várias estruturas de dados, como strings, hashes, listas, conjuntos, conjuntos ordenados com consultas de intervalo, bitmaps, hyperloglogs, índices geoespaciais e streams. Redis é frequentemente usado para caching, gerenciamento de sessões, análises em tempo real, correio de mensagens e muito mais.

## Como Executar

Para executar o projeto, certifique-se de ter o Python instalado juntamente com a biblioteca `redis-py`. Você também precisará de acesso a um servidor Redis. Atualize o host, a porta e a senha no bloco `__main__` do script com os detalhes do seu servidor Redis.

```python
if __name__ == "__main__":
    task_manager = TaskManager(host='seu_host_redis', port=sua_porta_redis, password='sua_senha_redis')
```

## Em seguida, execute o script usando:
```
python task_manager.py

```

# Imagens

## Adicionar Tarefa:

<div style="display: flex; align-items: start; margin-bottom: 20px;">
    <img src="https://github.com/leonardojfrenner/AtividadeRedis/assets/115934024/327cf16d-20dd-4078-995c-3b9abad020f3" width="400px" style="margin-right: 20px;" />
    <p style="text-align: left;">Essa opção permite ao usuário adicionar uma nova tarefa ao sistema. O usuário precisa fornecer uma descrição para a tarefa que será adicionada.</p>
</div>

## Listar Tarefas:

<div style="display: flex; align-items: start; margin-bottom: 20px;">
    <p style="text-align: left;">Ao selecionar esta opção, o sistema exibirá uma lista de todas as tarefas atualmente registradas, juntamente com seus respectivos IDs e status (por padrão, as tarefas são listadas como "EM ANDAMENTO" se o status não for especificado de outra forma).</p>
    <img src="https://github.com/leonardojfrenner/AtividadeRedis/assets/115934024/b72b22c1-50b1-4a0c-84f2-5026d49d85fa" width="400px" style="margin-left: 20px;" />
</div>

## Marcar Tarefa como Concluída:

<div style="display: flex; align-items: start; margin-bottom: 20px;">
    <img src="https://github.com/leonardojfrenner/AtividadeRedis/assets/115934024/1400cded-b7f1-4b88-8619-8377ecfbe0a1" width="400px" style="margin-right: 20px;" />
    <p style="text-align: left;">Essa opção permite ao usuário marcar uma tarefa específica como concluída. O usuário precisa fornecer o ID da tarefa que deseja marcar como concluída.</p>
</div>

## Remover Tarefa:

<div style="display: flex; align-items: start; margin-bottom: 20px;">
    <p style="text-align: left;">Ao escolher esta opção, o usuário pode remover uma tarefa específica do sistema. Para isso, é necessário fornecer o ID da tarefa que deseja remover.</p>
    <img src="https://github.com/leonardojfrenner/AtividadeRedis/assets/115934024/9eaa71fd-70cf-4b01-869f-83a51e09c0b2" width="400px" style="margin-left: 20px;" />
</div>

## Remover Todas as Tarefas:

<div style="display: flex; align-items: start; margin-bottom: 20px;">
    <img src="https://github.com/leonardojfrenner/AtividadeRedis/assets/115934024/b011911c-fa99-49ca-8e4a-2a69f1bdd355" width="400px" style="margin-right: 20px;" />
    <p style="text-align: left;">Esta opção remove todas as tarefas do sistema, reiniciando-o. É útil quando se deseja limpar todas as tarefas registradas.</p>
    <img src="https://github.com/leonardojfrenner/AtividadeRedis/assets/115934024/d1d373fc-55cf-4b21-8390-733f63273dec" width="400px" style="margin-left: 20px;" />
</div>

---

Obrigado por usar  meu Gerenciador de Tarefas! Espero que este projeto seja útil para você entender da praticidade de implementacão desse projeto com phyton e Redis. Se tiver alguma dúvida ou sugestão, não hesite em entrar em contato.

Tenha um ótimo dia e até logo!
