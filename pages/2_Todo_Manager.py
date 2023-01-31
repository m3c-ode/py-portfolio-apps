import streamlit as st
import functions

# version with completed multiple todos

st.set_page_config(layout="wide")


def add_todo():
    newTodo = st.session_state["newTodo"]
    todos.append(newTodo.title() + "\n")
    functions.addTodoToFile(todos)
    st.session_state["newTodo"] = ""


def complete_todos():
    """remove items to be deleted from todos and return list of items to be deleted"""
    del_key_list = []

    global todos
    print("todos", todos)
    todos_copy = todos[:]
    todos_copy.reverse()
    print("todos revq", todos_copy)
    list_len = len(todos)
    for index, todo in enumerate(todos):
        if st.session_state[f"cb_{index}"]:
            del_key_list.append(f"cb_{index}")
            todos_copy.pop(list_len - (index + 1))

    print("del key list", del_key_list)
    print("todos copy del", todos_copy)
    functions.addTodoToFile(reversed(todos_copy))

    return del_key_list


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
    checkbox = st.checkbox(todo, key=f"cb_{todos.index((todo))}")
    # if checkbox == True:
    #     del st.session_state[todo]
    #     todos.pop(todos.index(todo))
    #     functions.addTodoToFile(todos)
    #     st.experimental_rerun()

newTodo = st.text_input(
    "todo",
    label_visibility="hidden",
    placeholder="Enter new or edit todo...",
    key="newTodo",
    on_change=add_todo,
)

# add completed
st.button("Delete Completed", key="completed_todo")

if st.session_state["completed_todo"]:
    del_todos = complete_todos()
    if del_todos:
        for item in del_todos:
            del st.session_state[item]
            st.experimental_rerun()
