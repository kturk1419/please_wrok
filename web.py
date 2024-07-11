import streamlit as st
import methods

"""again"""
todos = methods.getTodos()

def clear_text():
    st.session_state.my_text = st.session_state.new_todo
    st.session_state.new_todo = ""
def add_todo():
    ntodo = st.session_state["new_todo"]
    todos.append(ntodo + "\n")
    methods.writeTodos(todos)
    clear_text()

def complete_todo():
    todo = st.session_state[""]

with st.container():
    st.title("TO DO APP")
    st.subheader("created by khaled turkestani")
    st.text("Organize your tasks here.")



with st.container():
    for i, todo in enumerate(todos):
        checkbox = st.checkbox(todo, key=todo)
        if checkbox:
            todos.pop(i)
            methods.writeTodos(todos)
            del st.session_state[todo]
            st.experimental_rerun()


with st.container():
    st.text_input("What do you want to do?",
                  placeholder="TODO",
                  on_change=add_todo,
                  key="new_todo")
