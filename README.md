# 🤖 AI Learning Chatbot

A **Python-based conversational chatbot** that dynamically learns new responses, analyzes user sentiment, and provides context-aware replies using **fuzzy string matching**.
It can respond to predefined queries, learn new answers from users, and personalize replies with emojis based on sentiment.

---

## 🧩 Features

* 💬 **Dynamic Learning:** Learns new responses from users in real-time.
* 🧠 **Sentiment Analysis:** Uses TextBlob to detect mood and adjust replies.
* 🔍 **Fuzzy Matching:** Handles typos and similar queries using RapidFuzz.
* 📂 **Persistent Memory:** Stores learned responses in `learned_responses.json`.
* 😊 **Emoji-Enhanced Responses:** Automatically adds emojis for positive/negative/neutral moods.
* ⚡ **Lightweight & Fast:** Runs entirely in the command-line interface.

---

## 🏗️ Project Structure

```
AI-Learning-Chatbot/
│
├── chatbot.py                  
├── responses.json              
├── learned_responses.json      
├── requirements.txt            
├── assets/                     
│   └── chatbot_screenshot.png  
└── README.md                   
```

---

## ⚙️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/Mamoonkhan11/Chatbot-with-python
cd Chatbot-with-python
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
source venv/bin/activate      # Linux/Mac
venv\Scripts\activate         # Windows
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

Dependencies include:

* **TextBlob** – For sentiment analysis
* **RapidFuzz** – For fuzzy string matching

### 4. Run the Chatbot

```bash
python chatbot.py
```

---

## 🧠 How It Works

1. **Load Responses:** Predefined responses from `responses.json` and any previously learned responses from `learned_responses.json`.
2. **User Input:** Chatbot receives input via CLI.
3. **Sentiment Analysis:** Detects user mood (positive, negative, neutral) using TextBlob.
4. **Fuzzy Matching:** Searches for the closest known question to provide a relevant answer.
5. **Learning:** If no match exists, chatbot asks the user for a new response and saves it for future use.
6. **Emoji Feedback:** Adds emoji depending on sentiment for personalized replies.

---

## 💬 Example Interaction

```
🤖 Chatbot: Hello! Type 'bye' to exit.
You: Hello
🤖 Chatbot: Hi there! 😊
You: I feel sad
🤖 Chatbot: I’m sorry to hear that. Hope things get better ❤️
You: What is AI?
🤖 Chatbot: I don’t know how to respond. What should I reply next time?
🧠 Teach me: AI stands for Artificial Intelligence
🤖 Chatbot: Got it! I’ll remember that for next time.
```

---

## 🔒 Notes

* Always keep `learned_responses.json` to persist chatbot knowledge.
* The bot’s learning is **case-insensitive** and stores responses in lowercase.
* Predefined responses are stored in `responses.json` and can be edited manually.

---

## 📈 Future Enhancements

* 🌐 Add a **web-based or GUI interface**
* 🗣️ **Voice input/output** support
* 📊 **Analytics dashboard** for conversation insights
* 🤖 Integrate with **GPT API** for smarter responses

---