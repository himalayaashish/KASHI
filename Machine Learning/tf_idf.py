from sklearn.feature_extraction.text import TfidfVectorizer

vectorizer = TfidfVectorizer()

data = ["This is good time","This is bad time this is","This this is best time","This is not worse time time"]

tfidf = vectorizer.fit_transform(data)

print(tfidf)
print('\n')
#(1, 5)	2   ==> In document number 1 word number 5 has occured 2 times    ----------------- This is bad time this is ----- is --->> 2

print(vectorizer.get_feature_names()) # This will give the words vectors (). i.e unique words
words = vectorizer.vocabulary_
print('\n')
print(words) # this will give thhe word with position.
