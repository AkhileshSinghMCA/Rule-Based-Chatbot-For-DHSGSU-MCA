import numpy as np
import nltk
from nltk.stem.porter import PorterStemmer
from nltk.corpus import stopwords

# Download necessary NLTK data
nltk.download('punkt')
nltk.download('stopwords')

# Initialize stemmer and stopwords
stemmer = PorterStemmer()
stop_words = set(stopwords.words('english'))

# Function to tokenize a sentence
def tokenize(sentence):
    tokens = nltk.word_tokenize(sentence)
    tokens = [token for token in tokens if token.isalnum() and token.lower() not in stop_words]
    return tokens

# Function to stem a word
def stem(word):
    return stemmer.stem(word.lower())

# Function to create a bag of words array
def bag_of_words(tokenized_sentence, words):
    sentence_words = [stem(word) for word in tokenized_sentence]
    bag = np.zeros(len(words), dtype=np.float32)
    for idx, w in enumerate(words):
        if w in sentence_words:
            bag[idx] = 1
    return bag

# Example usage
if __name__ == "__main__":
    sentence = "Hello! How are you doing today? Organizing the event was tough."
    words = ["hi", "hello", "I", "you", "bye", "thank", "cool", "organ", "event", "tough"]

    tokenized_sentence = tokenize(sentence)
    print(f"Tokenized Sentence: {tokenized_sentence}")

    bog = bag_of_words(tokenized_sentence, words)
    print(f"Bag of Words: {bog}")
