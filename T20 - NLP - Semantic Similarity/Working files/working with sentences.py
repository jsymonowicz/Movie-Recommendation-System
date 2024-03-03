import spacy
nlp = spacy.load('en_core_web_md')

sentences = ["where did my dog go",
             "Hello, there is my car",
             "I\'ve lost my car in my car",
             "I\'d like my boat back",
             "I will name my dog Diana"
             ]

model_sentence = nlp("Why is my cat on the car")
print(model_sentence)

for i in sentences:
    sim = nlp(i).similarity(model_sentence)
    print(f"{i}: {sim}")