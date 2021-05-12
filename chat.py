# chat initialization
model = load_model("chatbot_model.h5")
intents = json.loads(open("/intentrestr.json").read())
words = pickle.load(open("words.pkl", "rb"))
classes = pickle.load(open("classes.pkl", "rb"))
