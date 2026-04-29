import streamlit as st
st.title("My Streamlit APP")

user='abcd'
password = '1234'

u= st.text_input("Enter your name")
p= st.text_input("Enter your password")
# p=st.number_input("Enter your password")

if st.button("Login"):
    if user==u and password==p:
        st.write("Login Sucessfull")
    else:
        st.write("Try again")