# 🍽️ Restaurant AI Chatbot

An AI-powered Restaurant Chatbot built using **Streamlit** and **Groq (LLaMA model)** that allows users to interact with a virtual restaurant assistant.

🔗 **Live Demo:**  
https://restaurantaichatbot.streamlit.app/

---

## 🚀 About the Project

This project is an interactive chatbot designed to simulate a real restaurant assistant. Users can:

- Ask about menu items 🍛  
- Check prices 💰  
- Get food recommendations 🤖  
- Know restaurant timings ⏰  
- Ask location-related queries 📍  

The chatbot uses the **LLaMA 3.1 model via Groq API** to generate intelligent and context-aware responses.

---

## 🧠 How It Works

- The chatbot maintains conversation history using `st.session_state`
- All user messages are sent to the LLM along with previous context
- A **custom system prompt** defines restaurant details like menu, pricing, and behavior
- The AI responds like a **real restaurant assistant**

---

## 🛠️ Tech Stack

- **Frontend:** Streamlit  
- **Backend/LLM API:** Groq  
- **Model:** LLaMA 3.1 (8B Instant)  
- **Deployment:** Streamlit Cloud  
- **Environment Management:** dotenv + Streamlit Secrets  

---

## ✨ Features

- 💬 Real-time chat interface  
- 🧠 Context-aware conversation (chat memory)  
- 🍽️ Predefined restaurant menu and pricing  
- 🤖 AI-powered recommendations  
- 🔐 Secure API key handling  

---

## 📸 Screenshots / Demo

<img width="1375" height="1032" alt="{5CDC0087-618D-4F8B-B047-90EEAD93A743}" src="https://github.com/user-attachments/assets/c1d57c93-9762-41fa-a112-b8dafe32dde7" />

