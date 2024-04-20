import streamlit as st
from main import doTranslate

st.title("Translator App")
input_text = st.text_input('Enter the text to translate')

if input_text is not None:
    if st.button('Translate'):
        result = doTranslate(input_text)
        st.markdown(f"{result}")