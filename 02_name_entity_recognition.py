import spacy

nlp = spacy.load("en_core_web_sm")

# Sample text - "Apple Inc. is planning to open a new store in San Francisco. Tim Cook is the CEO of Apple."

if __name__ == "__main__":
    while True:
        input_text = input("Enter the text for entity recognition (type 'exit' to end): ")

        if input_text.lower() == 'exit':
            print("Exiting...")
            break

        doc = nlp(input_text)

        for ent in doc.ents:
          print(f"Entity: {ent.text}, Type: {ent.label_}")