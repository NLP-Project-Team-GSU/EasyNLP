from langdetect import detect
from nltk.tokenize import word_tokenize


# Common function for language detection
def detect_language(text):
    try:
        language = detect(text)
        if language != 'en':
            return None, "Only English text is supported"
        return language, None
    except Exception as e:
        return None, str(e)


# Common function for word count limit check
def check_word_count(text, WORD_COUNT_LIMIT=100):
    try:
        token_count = len(word_tokenize(text))
        if token_count > WORD_COUNT_LIMIT:
            return False, f"Word count exceeds limit ({token_count} > {WORD_COUNT_LIMIT})"
        return True, None
    except Exception as e:
        return False, str(e)
