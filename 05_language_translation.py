from googletrans import Translator

# Sample text - "Hello, how are you doing?"

if __name__ == "__main__":
    while True:
        input_text = input("Enter the text for translation (type 'exit' to end): ")

        if input_text.lower() == 'exit':
            print("Exiting...")
            break

        translator = Translator()
        translated_text = translator.translate(input_text, dest='fr').text

        print(f"Original Text: {input_text}")
        print(f"Translated Text: {translated_text}")

