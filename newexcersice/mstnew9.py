from textblob import TextBlob


sentence='dhaivat'

word=TextBlob(sentence)

result=word.correct()

print(result)