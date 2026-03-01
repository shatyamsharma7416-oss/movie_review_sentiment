import re
import nltk
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
nltk.download('wordnet')
nltk.download('punkt_tab')

def clean_tokenize(text):
  # Remove URLs
  text = re.sub(r'http\S+|www\.\S+', '', text)

  # Remove control characters
  text = re.sub(r'[\x00-\x1F\x7F-\x9F]', '', text)

  # Remove HTML tags
  text = re.sub(r'<[^>]+>', '', text)

  # Remove punctuation
  text = re.sub(r'[^a-z\s]', ' ', text)
  
  # Lemmatize and Tokenize
  lemmatizer = WordNetLemmatizer()
  text = word_tokenize(text)
  text = [lemmatizer.lemmatize(word, pos='v') for word in text]

  return text


