import streamlit as st
from groq import Groq
import os
from dotenv import load_dotenv

load_dotenv()

client = Groq(api_key = os.getenv("RESTAURANT_API_KEY"))

st.title("Restaurant ChatBot")

if "messages" not in st.session_state:
  st.session_state.messages = []

for msg in st.session_state.messages:
  with st.chat_message(msg["role"]):
    st.markdown(msg["content"])


user_input = st.chat_input("How may I help you?")

if user_input: 
  st.chat_message("user").markdown(user_input)
  st.session_state.messages.append({"role":"user", "content": user_input})

  response = client.chat.completions.create(
    model = "llama-3.1-8b-instant",
    messages = st.session_state.messages
  )

  ai_reply = response.choices[0].message.content

  st.chat_message("assistant").markdown(ai_reply)
  st.session_state.messages.append({"role": "assistant", "content": ai_reply})
