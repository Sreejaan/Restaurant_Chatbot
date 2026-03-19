import streamlit as st
from groq import Groq
import os
from dotenv import load_dotenv

load_dotenv()

client = Groq(api_key = st.secrets["RESTAURANT_API_KEY"])

st.title("Restaurant ChatBot")

if "messages" not in st.session_state:
    st.session_state.messages = [
        {
            "role": "system",
            "content": """
You are a helpful and friendly restaurant assistant for "Spice Garden Restaurant".

Here are the details of the restaurant:

📍 Location:
123 MG Road, Bangalore, India

🕒 Opening Hours:
Monday - Sunday: 10:00 AM to 11:00 PM

🍽️ Menu:

Starters:
- Paneer Tikka - ₹250
- Chicken Lollipop - ₹300
- Veg Spring Rolls - ₹200

Main Course:
- Butter Chicken - ₹400
- Paneer Butter Masala - ₹350
- Veg Biryani - ₹300
- Chicken Biryani - ₹350

Breads:
- Butter Naan - ₹40
- Garlic Naan - ₹60
- Tandoori Roti - ₹30

Beverages:
- Masala Chai - ₹50
- Cold Coffee - ₹120
- Fresh Lime Soda - ₹80

Desserts:
- Gulab Jamun - ₹100
- Ice Cream - ₹90

🎯 Your role:
- Help users with menu, prices, and recommendations
- Suggest dishes based on preferences
- Answer questions about timings and location
- Be polite and conversational
- Keep answers short and helpful
"""
        }
    ]

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
