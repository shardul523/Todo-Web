import streamlit as st
from todos_util import *

todos = get_todos()


def update_todos():
    new_todo = st.session_state["todo_in"] + "\n"
    st.session_state["todo_in"] = ""
    todos.append(new_todo)
    set_todos(todos)


st.title("My Todo App")  # Adds a heading
st.subheader("Developed by Shardul Sisodiya")  # Adds a subheading
st.write("Boost your productivity!")  # Adds simple text

for i, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=(todo + str(i)))
    if checkbox:
        todos.pop(i)
        set_todos(todos)
        del st.session_state[todo + str(i)]
        st.experimental_rerun()

st.text_input(label="", placeholder="Add new todo", on_change=update_todos, key="todo_in")  # Adds an
# input box


# st.session_state
