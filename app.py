# Streamlit Modern Chatbot UI with Emotional Learning Responses + Background Image

import streamlit as st
import json
import os
from textblob import TextBlob
from rapidfuzz import fuzz, process
import time
import base64



# --- Load responses ---
with open("responses.json") as f:
    responses = json.load(f)

if os.path.exists("learned_responses.json"):
    with open("learned_responses.json") as f:
        learned_responses = json.load(f)
else:
    learned_responses = {}

all_responses = {**responses, **learned_responses}



# --- Helper Functions ---
def save_learned_response(question, answer):
    learned_responses[question] = answer
    with open("learned_responses.json", "w") as f:
        json.dump(learned_responses, f, indent=4)

def analyze_sentiment(text):
    polarity = TextBlob(text).sentiment.polarity
    if polarity > 0.2:
        return "positive"
    elif polarity < -0.2:
        return "negative"
    else:
        return "neutral"

def get_best_match(user_input):
    all_keys = list(all_responses.keys())
    best_match, score, _ = process.extractOne(
        user_input.lower(), all_keys, scorer=fuzz.token_sort_ratio
    )
    return (best_match, score) if score >= 60 else (None, 0)

def respond(user_input):
    mood = analyze_sentiment(user_input)
    best_match, score = get_best_match(user_input)
    if best_match:
        base_response = all_responses[best_match]
        if mood == "positive":
            return base_response + " 😊"
        elif mood == "negative":
            return "I’m sorry to hear that. " + base_response + " ❤️"
        else:
            return base_response
    else:
        return None



# --- Streamlit UI ---
st.set_page_config(page_title="ChatBot Friend", page_icon="🤖", layout="wide")



# --- Background Image ---
def get_base64(file):
    with open(file, "rb") as f:
        return base64.b64encode(f.read()).decode()

background_base64 = get_base64(r"E:/Chatbot with python/BLOG-CONVERSATION-STUDIO-3.webp")



# --- Modern UI Styling ---
st.markdown(f"""
<style>
.stApp {{
    background-image: linear-gradient(rgba(0,0,0,0.75), rgba(0,0,0,0.75)), url("data:image/webp;base64,{background_base64}");
    background-size: cover;
    background-position: center;
    background-attachment: fixed;
    color: white;
    font-family: 'Poppins', sans-serif;
}}
.main-container {{
    max-width: 800px;
    margin: auto;
    padding-bottom: 120px;
    max-height: 75vh;
    overflow-y: auto;
    display: flex;
    flex-direction: column-reverse;
}}
.chat-bubble {{
    border-radius: 20px;
    padding: 12px 18px;
    margin: 10px 0;
    display: inline-block;
    font-size: 16px;
    word-wrap: break-word;
    line-height: 1.4;
}}
.user {{
    background: linear-gradient(135deg, #ff6a00, #ee0979);
    box-shadow: 0 0 12px rgba(255, 106, 0, 0.6);
    color: #fff;
    align-self: flex-end;
}}
.bot {{
    background: linear-gradient(135deg, #0072ff, #00c6ff);
    box-shadow: 0 0 12px rgba(0, 114, 255, 0.6);
    color: #fff;
    align-self: flex-start;
}}
.typing span {{
    animation: blink 1s infinite;
    font-weight: bold;
}}
@keyframes blink {{
    0%, 100% {{ opacity: 0; }}
    50% {{ opacity: 1; }}
}}
.bottom-bar {{
    position: fixed;
    bottom: 25px;
    left: 50%;
    transform: translateX(-50%);
    width: 70%;
    background: rgba(22, 27, 34, 0.85);
    border: 1px solid rgba(255, 255, 255, 0.1);
    border-radius: 40px;
    display: flex;
    align-items: center;
    padding: 10px 18px;
    box-shadow: 0 0 20px rgba(0,0,0,0.6);
    z-index: 1000;
}}
input[type="text"] {{
    background: transparent !important;
    border: none !important;
    outline: none !important;
    color: #fff !important;
    font-size: 16px !important;
    flex: 1;
}}
.stButton > button {{
    background: linear-gradient(90deg, #6a11cb, #2575fc);
    border: none;
    border-radius: 50%;
    color: white;
    font-size: 20px;
    padding: 0.4rem 0.6rem;
    transition: all 0.3s ease;
}}
.stButton > button:hover {{
    transform: scale(1.1);
}}
::-webkit-scrollbar {{
    width: 0px;
}}
</style>
""", unsafe_allow_html=True)



# --- Header ---
st.markdown("<h2 style='text-align:center; color:#00c6ff;'>🤖 Modern ChatBot Friend</h2>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center; color:#8b949e;'>Interactive | Emotional | Learning</p>", unsafe_allow_html=True)



# --- Initialize chat ---
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []



# --- Send message on Enter ---
def send_message():
    user_input = st.session_state.user_input.strip()
    if user_input:
        st.session_state.chat_history.append(("You", user_input))


        # Show typing indicator
        placeholder = st.empty()
        placeholder.markdown('<div class="Thinking...">Thinking...<span>.</span><span>.</span><span>.</span></div>', unsafe_allow_html=True)
        time.sleep(1.2)


        # Bot response
        response = respond(user_input)
        if response:
            st.session_state.chat_history.append(("Bot", response))
        else:
            st.session_state.chat_history.append(("Bot", "Hmm, I don’t know that yet 🤔. Teach me something new!"))

        placeholder.empty()
        st.session_state.user_input = ""



# --- Chat Container ---
chat_container = st.container()
with chat_container:
    st.markdown("<div class='main-container'>", unsafe_allow_html=True)
    for role, message in reversed(st.session_state.chat_history):
        if role == "You":
            st.markdown(f"<div class='chat-bubble user'>User:   {message}</div>", unsafe_allow_html=True)
        else:
            st.markdown(f"<div class='chat-bubble bot'>ChatBot:   {message}</div>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)



# --- Input Bar ---
st.markdown("<div class='bottom-bar'>", unsafe_allow_html=True)
col1, col2 = st.columns([8, 1])
with col1:
    st.text_input(
        "What do you want to say?",
        key="user_input",
        label_visibility="collapsed",
        on_change=send_message,
        placeholder="What do you want to say?",
    )
with col2:
    if st.button("➤"):
        send_message()
st.markdown("</div>", unsafe_allow_html=True)