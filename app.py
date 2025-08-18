# app.py
import streamlit as st
from main import ask_agent

st.set_page_config(page_title="Smart AI Assistant", layout="centered")
st.title("🤖 Autonomous AI Agent")

query = st.text_input("Type your request:")
if query:
    with st.spinner("Thinking..."):
        response = ask_agent(query)
        st.success(response)
