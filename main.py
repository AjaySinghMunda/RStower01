import streamlit as st



st.html("""
    <style>
        .stApp {
            background: #314755;  /* fallback for old browsers */
            background: -webkit-linear-gradient(to right, #26a0da, #314755);  /* Chrome 10-25, Safari 5.1-6 */
            background: linear-gradient(to right, #26a0da, #314755); /* W3C, IE 10+/ Edge, Firefox 16+, Chrome 26+, Opera 12+, Safari 7+ */

        }
    </style>
""")


st.logo(image="code.png", size="large")


st.title("All the basic python code")
t1=st.text_input("Username")
t2=st.text_input("Password",type="password")
b1=st.button("SIGNIN")
