import streamlit as st

# Page settings
st.set_page_config(page_title="Week 2 Python Project", page_icon="🐍")

st.title("🐍 Python Project 2")
st.write("This project explains why we selected PyCharm as our IDE. "
         "It also explains the difference between code editors and IDEs. ")

# ----------------------
# 1. WHY PYCHARM
# ----------------------
with st.expander("Why We Selected PyCharm", expanded=False):
    st.markdown("""
    <div style='background-color:#f0f7ff;padding:15px;border-radius:10px;'>
    <h3 style='color:#0066cc;'>Why We Selected PyCharm</h3>
    </div>
    """, unsafe_allow_html=True)

    st.write("""
    We selected PyCharm because it is easy to use.  
    It supports beginners.  
    It has many tools in one place.  
    It helps us write better Python code with less effort.
    """)

    st.subheader("Simple reasons why PyCharm is better")
    st.write("""
    1. It shows errors while typing.  
    2. It gives suggestions for functions and variables.  
    3. It has a built in debugger.  
    4. It supports virtual environments.  
    5. It manages libraries easily.  
    6. It has a nice interface with clear options.
    """)

# ----------------------
# 2. Pycharm vs Others
# ----------------------
with st.expander("PyCharm vs Other IDEs", expanded=False):
    st.markdown("""
    <div style='background-color:#ffe8f0;padding:15px;border-radius:10px;'>
    <h3 style='color:#cc0055;'>PyCharm vs Other IDEs</h3>
    </div>
    """, unsafe_allow_html=True)

    st.write("""
    Other IDEs are also good.  
    But PyCharm focuses only on Python.  
    This makes it clean and easy for students.

    Some IDEs try to support many languages.  
    They become confusing for beginners.  
    PyCharm keeps things simple and clear.
    """)

    st.write("""
    Example.  
    In Visual Studio Code you must install many extensions.  
    In PyCharm most features are already built in.  
    So beginners do not get confused.
    """)

# ----------------------
# 3. IDE vs CODE EDITOR
# ----------------------
with st.expander("Difference Between IDEs and Code Editors", expanded=False):
    st.markdown("""
    <div style='background-color:#fff7d6;padding:15px;border-radius:10px;'>
    <h3 style='color:#cc8a00;'>Difference Between Code Editors and IDEs</h3>
    </div>
    """, unsafe_allow_html=True)

    st.write("""
    A code editor is only for writing code.  
    It is simple.  
    It highlights keywords.  
    But it does not have extra tools.

    Examples. Notepad++. VS Code. Sublime Text.

    An IDE is a complete tool.  
    It includes editor, debugger, project tools, test tools, and environment support.  
    It is like a full workspace.

    Examples. PyCharm. Eclipse. IntelliJ.
    """)

# ----------------------
# 4. Features of IDEs
# ----------------------
with st.expander("What IDEs Can Do", expanded=False):
    st.subheader("Simple examples of what IDEs can do")
    st.write("""
    - Run code inside the IDE  
    - Debug code  
    - Manage files in projects  
    - Install packages  
    - Test code  
    - Format code  
    """)

# ----------------------
# 5. Disadvantages
# ----------------------
with st.expander("Disadvantages of PyCharm", expanded=False):
    st.markdown("""
    <div style='background-color:#ffe4e4;padding:15px;border-radius:10px;'>
    <h3 style='color:#990000;'>Disadvantages of PyCharm</h3>
    </div>
    """, unsafe_allow_html=True)

    st.write("""
    1. It uses more memory than small editors.  
    2. It takes longer to start.  
    3. Some features are paid.  
    """)

    st.subheader("Why these disadvantages do not matter much")
    st.write("""
    PyCharm gives many tools that save time.  
    So using more memory is fine.  
    The free Community Edition is enough for students.  
    Startup time is not a big issue because we work inside the IDE for long time.
    """)

# ----------------------
# 6. Beginner Tips
# ----------------------
with st.expander("Beginner Tips for PyCharm", expanded=False):
    st.markdown("""
    <div style='background-color:#e6ffee;padding:15px;border-radius:10px;'>
    <h3 style='color:#008040;'>Beginner Tips for PyCharm</h3>
    </div>
    """, unsafe_allow_html=True)

    st.write("""
    - Create a new project and explore folders.  
    - Write small programs first.  
    - Use Run button on top.  
    - Use Terminal inside PyCharm to install packages.  
    - Try the debugger once to understand how code runs line by line.
    """)

# ----------------------
# 7. Code Example
# ----------------------
with st.expander("Small Python Example", expanded=False):
    st.subheader("Small Python Example")
    st.code("""
def greet(name):
    print("Hello", name)

greet("Tanush")
""")

# Footer
st.write("---")
st.write("End of Project. Thank you.")
