from googletrans import Translator
from language_mapping import language_codes

# Sample text - "Hello, how are you doing?"

if __name__ == "__main__":
    while True:
        input_text = input("Enter the text for translation (type 'exit' to end): ")

        if input_text.lower() == 'exit':
            print("Exiting...")
            break
        
        while True:
            dest_language_name = input("Enter the destination language (e.g., 'French'): ").capitalize()

            try:
                dest_language_code = language_codes[dest_language_name]
                break  # Break out of the inner loop if a valid language code is found
            except KeyError:
                print("Invalid language name. Please try again.")

        translator = Translator()
        translated_text = translator.translate(input_text, dest=dest_language_code).text

        print(f"Original Text: {input_text}")
        print(f"Translated Text: {translated_text}")

