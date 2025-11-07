import streamlit as st
from datetime import datetime

st.set_page_config(page_title="My Python Application", layout="centered")

st.markdown("## ====================================")
st.markdown("###     Welcome to my Application!     ")
st.markdown("## ====================================")

name = st.text_input("Please enter your name:")

if name:
    current_time = datetime.now()
    formatted_time = current_time.strftime("%d %B %Y, %I:%M %p")

    st.markdown("---")
    st.subheader("USER DETAILS")
    st.write(f"**Hello, {name}!**")
    st.write(f"**Current Date and Time:** {formatted_time}")

    if st.button("Continue"):
        st.markdown("""
        ---
        ## 🧠 PYTHON FEATURE: EXTENSIVE LIBRARIES
        ---

        ### 1️⃣ INTRODUCTION TO LIBRARIES
        A library is a collection of pre-written code that helps programmers
        perform common tasks without writing code from scratch.

        Python has over **450,000+ packages** on the Python Package Index (PyPI),
        covering almost every field — AI, data analysis, automation, and web development.

        ---

        ### 2️⃣ LIBRARIES USED IN ARTIFICIAL INTELLIGENCE & MACHINE LEARNING
        - **TensorFlow** → Deep learning (Google)
        - **Keras** → User-friendly, built on TensorFlow  
        - **Scikit-learn** → Regression, clustering, classification  
        - **PyTorch** → Research & AI labs (Meta)

        ```python
        from sklearn.linear_model import LinearRegression
        model = LinearRegression()
        model.fit([[1],[2],[3]], [2,4,6])
        print(model.predict([[4]]))
        ```

        ---

        ### 3️⃣ LIBRARIES USED IN WEB DEVELOPMENT
        - **Flask** → Lightweight web framework  
        - **Django** → Full-stack framework used by platforms like Instagram

        ```python
        from flask import Flask
        app = Flask(__name__)

        @app.route('/')
        def home():
            return "Hello, World!"

        app.run()
        ```

        ---

        ### 4️⃣ LIBRARIES USED IN UI & DESKTOP APPLICATIONS
        - **Tkinter** → Built-in GUI library  
        - **PyQt** → Professional desktop apps  
        - **Kivy** → Cross-platform apps (desktop + mobile)

        ---

        ### 5️⃣ PROS AND CONS OF PYTHON LIBRARIES
        **Advantages:**
        - Saves time using ready-made code  
        - Reduces errors & improves efficiency  
        - Huge community support  
        - Enables complex tasks with fewer lines  

        **Limitations:**
        - Too many libraries can confuse beginners  
        - Some require manual installation  
        - Heavy libraries can slow small projects  

        ---

        ### 🎯 CONCLUSION
        Python libraries make programming easier, faster, and more powerful.  
        They let developers focus on **logic and creativity** instead of rewriting basic features.  
        This is one of the main reasons **Python remains one of the world’s most popular languages.**

        ---
        """)
        st.success("✅ Thank you for visiting!")