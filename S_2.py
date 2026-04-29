# Calculate Percentage of 5 subject marks

import streamlit as st
st.title("Calculator APP")

s1= st.number_input("Enter English marks")
s2= st.number_input("Enter SQL Marks")
s3= st.number_input("Enter Python marks")
s4= st.number_input("Enter Excel Marks")
s5= st.number_input("Enter ML marks")

if st.button("Calculator"):
   t=s1+s2+s3+s4+s5

   p= t/500*100
   st.write("Your percentage is =",p)