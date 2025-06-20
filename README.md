# ChatBot

Key Components:
app.py: Main Flask application entry point.

chatbot.py: Core chatbot logic.

intents.py: Contains user intents and their mappings.

preprocess.py: Handles text preprocessing (likely NLP tasks).

similarity.py: Computes text similarity (probably for matching user queries with intents).

templates/index.html: Web interface for the chatbot.

static/ima2.jpeg: Static resource (likely used in the UI).

.idea/: IDE-specific config files (can be excluded from README).


ChatBot/
├── app.py # Flask app entry point
├── chatbot.py # Core chatbot logic
├── intents.py # Intent-response structure
├── preprocess.py # Text preprocessing (tokenization, stemming)
├── similarity.py # Cosine similarity calculation
├── templates/index.html # Chatbot UI
├── static/ima2.jpeg # Image for the UI
└── pycache/ # Compiled Python files


 Notes
Customize intents.py to add new chatbot responses.

Designed for educational/demo purposes — not production-ready.
