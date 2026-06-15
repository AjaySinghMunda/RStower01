import streamlit as st

st.title("Check which number is greater.")

st.logo(image="code.png", size="large")

t1 = st.text_input("Enter a number")

t2 = st.text_input("Enter another number")

b1 = st.button("Check")


if b1 :
    
    if t1 != "" and t2 != "" :
        
        
        n1 = int(t1)
        n2 = int(t2)
    
        if n1 > n2 :
            st.success(f"The number {n1} is greater than {n2}")
        
        elif n1 == n2 :
            st.info("Both numbers are same.")
        
        else :
            st.success(f"The number {n2} is greater than {n1}")
    
    
    
        
    else :
      st.error("Please enter a number before checking.")
      
st.subheader("Code")

st.code("""
        
import streamlit as st

st.title("Check which number is greater.")

st.logo(image="code.png", size="large")

t1 = st.text_input("Enter a number")

t2 = st.text_input("Enter another number")

b1 = st.button("Check")


if b1 :
    
    if t1 != "" and t2 != "" :
        
        
        n1 = int(t1)
        n2 = int(t2)
    
        if n1 > n2 :
            st.success(f"The number {n1} is greater than {n2}")
        
        elif n1 == n2 :
            st.info("Both numbers are same.")
        
        else :
            st.success(f"The number {n2} is greater than {n1}")
    
    
    
        
else :
    st.error("Please enter a number before checking.")     
        
        
        
        
        
        
""", language="python")