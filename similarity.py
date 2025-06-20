from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from preprocess import preprocess_text
from intents import intents

def get_intent(user_input):
    max_similarity = 0
    best_intent = "default"
    user_input_processed = ' '.join(preprocess_text(user_input))

    vectorizer = TfidfVectorizer()

    for intent, data in intents.items():
        phrases = data["training_phrases"]
        phrases_processed = [' '.join(preprocess_text(phrase)) for phrase in phrases]

        all_phrases = phrases_processed + [user_input_processed]
        vectors = vectorizer.fit_transform(all_phrases).toarray()

        similarities = cosine_similarity([vectors[-1]], vectors[:-1])
        highest_similarity = similarities.max()

        if highest_similarity > max_similarity:
            max_similarity = highest_similarity
            best_intent = intent

    return best_intent
