import streamlit as st

st.set_page_config(page_title="Python Data Types Project", page_icon="💡", layout="centered")

# Title
st.title("💡 Project 3: Python Data Types vs Data Types in Other Languages")
st.write("This project explains all data types in Python. It also compares them with data types found in other programming languages like C, C++, Java and JavaScript.")

# ---------------------------
# SECTION 1: What are Data Types?
# ---------------------------
with st.expander("🌈 What are Data Types?"):
    st.markdown("""
    <div style='background-color:#f0f4ff;padding:15px;border-radius:10px;'>
    <h3 style='color:#003399;'>Understanding What Data Types Are</h3>
    </div>
    """, unsafe_allow_html=True)

    st.write("""
    A data type tells the computer what kind of value you are storing.  
    It tells how much memory to use and what operations you can perform.

    Example:  
    - 5 is an integer  
    - 3.14 is a floating number  
    - "hello" is a string  
    """)

# ---------------------------
# SECTION 2: Why Python is Different
# ---------------------------
with st.expander("🟦 Why Python Data Types Are Different"):
    st.markdown("""
    <div style='background-color:#e9ffe9;padding:15px;border-radius:10px;'>
    <h3 style='color:#00802b;'>Why Python Stands Out</h3>
    </div>
    """, unsafe_allow_html=True)

    st.write("""
    Python is different from languages like C, C++, and Java.  
    Here is why:

    1. Python is dynamically typed.  
       You do not write the data type manually.  
       Python figures it out automatically.

       Example in Python:  
       ```
       x = 10
       y = "Hello"
       ```
       Example in Java:  
       ```
       int x = 10;
       String y = "Hello";
       ```

    2. Python allows you to change the data type of a variable at any time.  
       ```
       x = 10
       x = "Now I am a string"
       ```

    3. Python has built-in very high level data types like lists, dictionaries, tuples, sets.  
       C and Java do not have these built in.

    4. Python makes data types easy to use without worrying about memory size.  
       In C, you must pick `int`, `short`, `long`, `float`, `double`, etc.  
       Python does this automatically.
    """)

# ---------------------------
# SECTION 3: Python Data Types (All of Them)
# ---------------------------
with st.expander("📘 Python Data Types (Detailed List)"):
    st.markdown("""
    <div style='background-color:#fff5e6;padding:15px;border-radius:10px;'>
    <h3 style='color:#cc6600;'>Python Data Types (Classified)</h3>
    </div>
    """, unsafe_allow_html=True)

    st.subheader("1. Numeric Types")
    st.write("""
    - **int** → whole numbers  
    - **float** → decimal values  
    - **complex** → numbers with imaginary part

    Example:
    ```
    a = 5
    b = 3.14
    c = 2 + 3j
    ```
    """)

    st.subheader("2. Text Type")
    st.write("""
    - **str** → strings or text  

    Example:
    ```
    name = "Tanush"
    ```
    """)

    st.subheader("3. Boolean Type")
    st.write("""
    - **bool** → True or False  
    """)

    st.subheader("4. Sequence Types")
    st.write("""
    - **list** → ordered, changeable  
    - **tuple** → ordered, unchangeable  
    - **range** → sequence of numbers

    Example:
    ```
    my_list = [1, 2, 3]
    my_tuple = (4, 5, 6)
    numbers = range(1, 10)
    ```
    """)

    st.subheader("5. Set Types")
    st.write("""
    - **set** → unordered, unique values  
    - **frozenset** → frozen version of set (unchangeable)
    """)

    st.subheader("6. Mapping Types")
    st.write("""
    - **dict** → key-value pairs

    Example:
    ```
    person = {"name": "Asha", "age": 20}
    ```
    """)

    st.subheader("7. Binary Types")
    st.write("""
    - **bytes**  
    - **bytearray**  
    - **memoryview**  
    """)

# ---------------------------
# SECTION 4: Comparison Table
# ---------------------------
with st.expander("📊 Python vs Other Languages (Side-by-Side Comparison)"):
    st.markdown("""
    <div style='background-color:#efffff;padding:15px;border-radius:10px;'>
    <h3 style='color:#006666;'>Comparison with Languages Like C, Java, JavaScript</h3>
    </div>
    """, unsafe_allow_html=True)

    st.write("""
    ### ✔ Python (Dynamic)
    - No need to declare type  
    - Easy to write  
    - Automatically adjusts size  
    - High-level types built in  

    ### ✔ Java (Static)
    - Must declare data types  
    - Strict  
    - No built-in lists or dictionaries like Python  
    - Uses arrays instead  

    ### ✔ C/C++ (Low-level)
    - Must manage memory manually  
    - Harder for beginners  
    - No built-in strings or lists  

    ### ✔ JavaScript
    - Dynamic like Python  
    - But fewer built-in complex data types  
    """)

# ---------------------------
# SECTION 5: Memory & Typing Difference
# ---------------------------
with st.expander("💾 Memory Management and Typing System"):
    st.markdown("""
    <div style='background-color:#fce6ff;padding:15px;border-radius:10px;'>
    <h3 style='color:#9900cc;'>Memory Differences</h3>
    </div>
    """, unsafe_allow_html=True)

    st.write("""
    Python automatically manages memory with a garbage collector.  
    C and C++ require you to free memory yourself.  
    Java also has garbage collection but requires type declaration.

    Python is dynamic.  
    C, C++, Java are static.  
    """)

# ---------------------------
# SECTION 6: Code Examples
# ---------------------------
with st.expander("🧪 Code Examples Showing Differences"):
    st.subheader("Python Example")
    st.code("""
x = 10
x = "hello"
print(x)
""")

    st.subheader("C Example")
    st.code("""
int x = 10;
x = "hello"; // error
""")

    st.subheader("Java Example")
    st.code("""
int x = 10;
String y = "hello";
""")

    st.subheader("JavaScript Example")
    st.code("""
let x = 10;
x = "hello"; // works
""")

# ---------------------------
# FOOTER
# ---------------------------
st.write("---")
st.write("End of Project 3. Thank you for reading!")

