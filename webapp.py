import streamlit as st
import functions

def add_tarefa():
    tarefa = st.session_state["nova_tarefa"] + "\n"
    tarefas.append(tarefa)
    functions.write_tarefas(tarefas)

tarefas = functions.get_tarefas()

st.title("Minha lista de Tarefas")

for index, tarefa in enumerate(tarefas):
    checkbox = st.checkbox(tarefa, key=tarefa)
    if checkbox:
        tarefas.pop(index)
        functions.write_tarefas(tarefas)
        del st.session_state[tarefa]
        st.experimental_rerun()

st.text_input(label="", placeholder="Digite uma nova tarefa."
              , on_change=add_tarefa, key='nova_tarefa')

