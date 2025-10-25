import json
import os
from textblob import TextBlob
from rapidfuzz import fuzz, process

# Load responses
with open("responses.json") as f:
    responses = json.load(f)

# Load learned responses
if os.path.exists("learned_responses.json"):
    with open("learned_responses.json") as f:
        learned_responses = json.load(f)
else:
    learned_responses = {}

# Combine both
all_responses = {**responses, **learned_responses}

def save_learned_response(question, answer):
    learned_responses[question] = answer
    with open("learned_responses.json", "w") as f:
        json.dump(learned_responses, f, indent=4)

def analyze_sentiment(text):
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity  # -1 to +1
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

def main():
    print("🤖 Chatbot: Hello! Type 'bye' to exit.")
    while True:
        user_input = input("You: ")
        if user_input.lower().strip() == "bye":
            print("🤖 Chatbot:", responses["bye"])
            break

        response = respond(user_input)
        if response:
            print("🤖 Chatbot:", response)
        else:
            print("🤖 Chatbot: I don’t know how to respond. What should I reply next time?")
            new_response = input("🧠 Teach me: ")
            save_learned_response(user_input.lower().strip(), new_response)
            all_responses[user_input.lower().strip()] = new_response
            print("🤖 Chatbot: Got it! I’ll remember that for next time.")

if __name__ == "__main__":
    main()