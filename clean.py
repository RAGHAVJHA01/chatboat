words = [lemmatizer.lemmatize(w.lower()) for w in words if w not in ignore_words]
# remove duplicates and sort
# remove duplicates
classes = sorted(list(set(classes)))
print(len(documents),'documents')
print(len(classes),'classes',classes)
print(len(words),'unique lemitize words',words)
pickle.dump(words, open("words.pkl", "wb"))
pickle.dump(classes, open("classes.pkl", "wb"))
