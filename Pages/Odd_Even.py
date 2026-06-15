import streamlit as st

st.logo(image="code.png", size="large")


st.title("Odd or Even")

n1 = st.text_input("Enter a number: ")

b1 = st.button("Check")

if b1:
    
    if n1 != "":
        
        t1 = int(n1)
        
        if t1 % 2 == 1:
           st.success("The number is odd.")
        
        else :
           st.success("The number is even.")
        
    else :
        st.error("Please enter a number before clicking Check.")
        
        
st.subheader("Code")

st.code("""
        
        
import streamlit as st


st.title("Odd or Even")

n1 = st.text_input("Enter a number: ")

b1 = st.button("Check")

if b1:
    
    if n1 != "":
        
        t1 = int(n1)
        
        if t1 % 2 == 1:
           st.success("The number is odd.")
        
        else :
           st.success("The number is even.")
        
    else :
        st.error("Please enter a number before clicking Check.")
        
        
        
        
""", language="python")