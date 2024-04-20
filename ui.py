import streamlit as st
from main import doTranslate

def setup_page():

    st.set_page_config(page_title="Streamlit Translator", page_icon="💱", layout="wide")

    st.title("Streamlit Translator")
    st.write("Translate text from English to your preferred language in real-time.")

def main():
    setup_page()

    input_text = st.text_area('Enter the text to translate', height=150)

    languages = {
        "French": "fr",
        "Spanish": "es",
        "German": "de",
        "Malayalam": "ml",
        "Hindi": "hi",
        "Chinese": "zh",
       
    }
    target_language = st.selectbox('Select target language:', list(languages.keys()))

    if st.button('Translate',type="primary"):
        if input_text:
            translated_text = doTranslate(input_text, languages[target_language])
            st.write(f"Translated text to {target_language}:")
            st.success(translated_text)
        else:
            st.warning("Please enter text to translate.")

if __name__ == "__main__":
    main()