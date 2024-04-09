import streamlit as st
import functions


def add_todo():
    todo = st.session_state['new_todo'] + '\n'
    todos.append(todo)
    functions.update_todos(todos)


todos = functions.get_todos()

st.title("My Todo App")
st.subheader("This is my todo app.")
st.write("I hope you enjoy! :)")

for index, item in enumerate(todos):
    checkbox = st.checkbox(item, key=item)
    if checkbox:
        todos.pop(index)
        functions.update_todos(todos)
        del st.session_state[item]
        st.rerun()

st.text_input(label="New To Do", placeholder="Add a new To Do...",
              on_change=add_todo, key='new_todo',
              label_visibility='hidden')
