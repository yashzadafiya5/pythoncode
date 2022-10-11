# Detect Questions using Python 

# from nltk.tokenize import word_tokenize
# question_words = ["what", "why", "when", "where", 
#              "name", "is", "how", "do", "does", 
#              "which", "are", "could", "would", 
#              "should", "has", "have", "whom", "whose", "don't"]

# question = input("Input a sentence: ")
# question = question.lower()
# question = word_tokenize(question)
# print(question)
# if any(x in question[0] for x in question_words):
#     print("This is a question!")
# else:
#     print("This is not a question!")
from nltk.tokenize import  word_tokenize

data = "Hello, Awesome User"

# tokenization of sentence into words
tokens = word_tokenize(data)

# printing the tokens
print(word_tokenize(data))
print(tokens)
