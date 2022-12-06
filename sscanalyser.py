import streamlit as st

st.title('SSC Result analyser')

Q = st.slider('How many questions you attemted in the entire paper?', 0,100,0,1)

A = st.slider('What is the percentage accuracy? ( in % )',0,100,0,5)

