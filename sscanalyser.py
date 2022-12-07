import streamlit as st

st.title('SSC Result analyser')

Q = st.slider('How many questions you attempted in the entire paper?', 0,100,0,1)

A = st.slider('What is the percentage OF CORRECT answers? ( in % )',0,100,0,5)

estimated = (A/100*Q)*2-((100-A)/100))*0.5*Q


"your approximate score is",estimated
