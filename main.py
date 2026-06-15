import streamlit as st

st.html("""
    <style>
        .stApp {
            background-color: #f0f2f6; /* Replace with your preferred hex color */
        }
    </style>
""")


st.logo(image="code.png", size="large")


st.title("All the basic python code")
t1=st.text_input("Username")
t2=st.text_input("Password",type="password")
b1=st.button("SIGNIN")
