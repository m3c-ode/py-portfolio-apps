import streamlit as st
import functions

st.set_page_config(layout="wide")


def add_todo():
    newTodo = st.session_state["newTodo"]
    todos.append(newTodo.title() + "\n")
    functions.addTodoToFile(todos)
    st.session_state["newTodo"] = ""


st.title("Todo Manager")
st.subheader("App to manage daily activities")
st.write(
    """ 
    <b>Organize</b> your day and increase your <b>productivity</b>.\n 
    Simply Enter a Todo in the textbox below, and Check the todos that you have completed!
    """,
    unsafe_allow_html=True,
)

todos = functions.showTodos()
for todo in todos:
    checkbox = st.checkbox(todo, key=todo)
    if checkbox == True:
        del st.session_state[todo]
        todos.pop(todos.index(todo))
        functions.addTodoToFile(todos)
        st.experimental_rerun()

newTodo = st.text_input(
    "todo",
    label_visibility="hidden",
    placeholder="Enter new or edit todo...",
    key="newTodo",
    on_change=add_todo,
)
