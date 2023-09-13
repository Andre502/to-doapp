FILEPATH = "tarefas.txt"

def get_tarefas(filepath=FILEPATH):
    """lê o arquivo txt e retorna a lista de tarefas."""
    with open(filepath, 'r') as file_local:
        tarefas_local = file_local.readlines()
    return tarefas_local

def write_tarefas(tarefas_arg, filepath=FILEPATH):
    """faz alterações na lista de tarefas."""
    with open(filepath, 'w') as file:
        file.writelines(tarefas_arg)

if __name__ == "__main__":
    print("Hello")
    print(get_tarefas())

