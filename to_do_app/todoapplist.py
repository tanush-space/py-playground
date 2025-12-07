import streamlit as st

st.set_page_config(page_title="To-Do List", layout="centered")
st.title("📝 To-Do List")

if "tasks" not in st.session_state:
    st.session_state.tasks = []

task = st.text_input("Add a new task")

c1, c2 = st.columns([1, 4])
with c1:
    add = st.button("Add")
with c2:
    clear = st.button("Clear Done")

if add and task:
    st.session_state.tasks.append({"task": task, "done": False})
    st.rerun()

if clear:
    st.session_state.tasks = [t for t in st.session_state.tasks if not t["done"]]
    st.rerun()

st.markdown("---")

for i, t in enumerate(st.session_state.tasks):
    a, b = st.columns([0.08, 0.92])
    with a:
        d = st.checkbox("", value=t["done"], key=f"chk_{i}", label_visibility="hidden")
    with b:
        if d:
            st.markdown(f"<div style='text-decoration:line-through; color:gray; padding-top:4px'>{t['task']}</div>", unsafe_allow_html=True)
        else:
            st.markdown(f"<div style='padding-top:4px'>{t['task']}</div>", unsafe_allow_html=True)
    st.session_state.tasks[i]["done"] = d
