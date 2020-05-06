from sklearn.feature_extraction.text import TfidfVectorizer

vectorizer = TfidfVectorizer()

#data = ["This is good time","This is bad time this is","This this is best time","This is not worse time time"]

data = ["The sky is blue","The sky is not blue"]

tfidf = vectorizer.fit_transform(data)

print(tfidf)
print('\n')

#(1, 4)	0.40909010368335985 ==> In document number 1 which is ["The skype is not blue"] word 4 which is 'The' TF-idf = 0.40909010368335985

print(vectorizer.get_feature_names()) # This will give the words vectors (). i.e unique words
words = vectorizer.vocabulary_
print('\n')
print(words) # this will give thhe word with position.

