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
- A custom system prompt defines restaurant details like menu, pricing, and behavior
- The AI responds like a real restaurant assistant

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

Example:<img width="1375" height="1032" alt="image" src="https://github.com/user-attachments/assets/f1e14b42-4869-4ef5-bf36-8ac856b269cf" />


---

## ⚙️ How to Run This Project Locally

Follow these steps to set up and run the project on your system:

### 1. Clone the Repository

```bash
git clone https://github.com/Sreejaan/Restaurant_Chatbot.git
cd Restaurant_Chatbot
````

### 2. Create a Virtual Environment (Recommended)

```bash
python -m venv venv
```

Activate it:

**Windows:**

```bash
venv\Scripts\activate
```

**Mac/Linux:**

```bash
source venv/bin/activate
```

### 3. Install Required Dependencies

```bash
pip install -r requirements.txt
```

### 4. Set Up API Key

Create a `.env` file in the root directory and add:

```env
RESTAURANT_API_KEY=your_groq_api_key_here
```

> Replace `your_groq_api_key_here` with your actual Groq API key.

### 5. Run the Application

```bash
streamlit run app.py
```

### 6. Open in Browser

After running the above command, open:

```
http://localhost:8501
```

---

