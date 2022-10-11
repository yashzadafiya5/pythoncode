# 21. Remove Cuss Words using Python 

from better_profanity import profanity
text = "please leave us i am so piss off"
censored = profanity.censor(text)
print(censored)