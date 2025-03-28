import streamlit as st # type: ignore

# Page configuration
st.set_page_config(
    page_title="To-Do App",
    layout="centered",
)

# Custom CSS
st.markdown(
    """
    <style>
    /* Style for the title */
    .custom-title {
        color: #4CAF50;
        font-size: 36px;
        text-align: center;
        font-family: 'Arial', sans-serif;
        text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.2);
    }

    /* Style for the input field */
    .custom-input input {
        border-radius: 10px;
        padding: 10px;
        font-size: 16px;
        border: 2px solid #4CAF50;
       
    }

    /* Style for the button */
    .custom-button button {
        background-color: #4CAF50;
        color: white;
        border-radius: 10px;
        padding: 10px 20px;
        border: none;
        font-size: 16px;
     
    }
    .custom-button button:hover {
        background-color: #45a049;
    }

    /* Style for the task container */
    .task-container {
        background-color: #f9f9f9;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Styled title
st.markdown('<h1 class="custom-title">To-Do App</h1>', unsafe_allow_html=True)

# Initialize session state for tasks
if "tasks" not in st.session_state:
    st.session_state.tasks = []

# Function to add a task
def add_task():
    task = st.session_state.task_input
    if task:
        st.session_state.tasks.append(task)
        st.session_state.task_input = ""  # Clear the input box

# Function to remove a task
def remove_task(index):
    st.session_state.tasks.pop(index)

# Input field with custom class
st.markdown('<div class="custom-input">', unsafe_allow_html=True)
task_input = st.text_input("Enter a task", key="task_input", placeholder="Add a new task...", label_visibility="collapsed")
st.markdown('</div>', unsafe_allow_html=True)

# Button with custom class
st.markdown('<div class="custom-button">', unsafe_allow_html=True)
st.button("Add Task", on_click=add_task, use_container_width=True)
st.markdown('</div>', unsafe_allow_html=True)

# Display tasks
if st.session_state.tasks:
    st.markdown('<div class="task-container">', unsafe_allow_html=True)
    st.write("### Your Tasks:")
    for i, task in enumerate(st.session_state.tasks):
        col1, col2 = st.columns([4, 1])
        with col1:
            st.markdown(f"✅ **{task}**")
        with col2:
            if st.button("Delete" ,  key=f"delete_{i}",):
                remove_task(i)
    st.markdown('</div>', unsafe_allow_html=True)
else:
    st.info("No tasks added yet. Add a task above!")