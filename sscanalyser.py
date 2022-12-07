import streamlit as st

st.title('SSC Result analyser')

Q = st.slider('How many questions you attemted in the entire paper?', 0,100,0,1)

A = st.slider('What is the percentage OF CORRECT answers? ( in % )',0,100,0,5)

wrong = 100-A
estimated = (2*(Q * (A/100)))-(wrong/100)*0.5


"your approximate score is",estimated
