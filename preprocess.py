import nltk
from nltk.stem import WordNetLemmatizer
import nltk
from nltk.stem import WordNetLemmatizer
import re

# Try to download common NLTK data quietly in dev. In serverless environments
# this may fail or be unavailable, so we provide a fallback tokenizer below.
try:
    nltk.download('punkt', quiet=True)
    nltk.download('wordnet', quiet=True)
except Exception:
    pass

lemmatizer = WordNetLemmatizer()

def preprocess_text(text):
    """Tokenize + lemmatize. Use NLTK when available, otherwise fall back.

    This avoids runtime crashes in serverless environments where NLTK data
    (punkt/wordnet) may not be present.
    """
    try:
        tokens = nltk.word_tokenize(text)
    except LookupError:
        # simple fallback tokenizer: keep alphanumeric words
        tokens = re.findall(r"\b\w+\b", text)

    result = []
    for token in tokens:
        tok = token.lower()
        if tok.isalnum():
            try:
                result.append(lemmatizer.lemmatize(tok))
            except Exception:
                result.append(tok)
    return result
