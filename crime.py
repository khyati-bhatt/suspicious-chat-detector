import streamlit as st
import input
import output


st.title("Suspicious Chat Detector")

file=st.file_uploader("Upload chat for analysis", type="txt")


if file:
    st.write("File Metadata:")
    st.write(f"File Name: {file.name}")
    st.write(f"File Size: {file.size} bytes")
    st.write(f"File Type: {file.type}")
    chat=file.read().decode('utf-8').splitlines()
    cleaned_chat = input.extract_text_messages(chat)
    st.write(cleaned_chat)
    is_illegal=output.check_illegal_chat(chat,output.model,output.vectorizer,threshold=0.2)
    if is_illegal:
        st.write("The chat is classified as illegal.")
    else:
        st.write("The chat is classified as legal.")
    
    
    
    




