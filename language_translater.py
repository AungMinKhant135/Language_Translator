import streamlit as st 
from googletrans import Translator

st.header("Language Translator")
translator = Translator()
fortext = st.text_input("Enter something to transtlate")
forcode = st.text_input("Enter a language code")

if st.button("Translate"):
    
    a = (translator.translate(fortext, dest=forcode).text)
    st.success(a)
else:
    st.write("press translate")