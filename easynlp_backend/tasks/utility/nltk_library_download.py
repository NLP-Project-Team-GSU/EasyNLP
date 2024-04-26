import nltk
import ssl

# Disable SSL certificate verification for NLTK
ssl._create_default_https_context = ssl._create_unverified_context

# Download NLTK data
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('averaged_perceptron_tagger')
