# init file
with open('/content/intentrestr.json', 'r') as f:
    intents = json.load(f)
words = []
classes = []
documents = []
ignore_words =['?','!','.']
for intent in intents['intents']:
  for pattern in intent['patterns']:
    #tokenize each word in the sentence
    w= nltk.word_tokenize(pattern)
    words.extend(w)
    documents.append((w,intent['tag']))
  if intent['tag'] not in classes:
    classes.append(intent['tag'])
