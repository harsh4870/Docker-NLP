from summarizer import Summarizer

# Sample text - "Artificial intelligence (AI) is a branch of computer science that aims to create machines capable of intelligent behavior. These machines are designed to mimic human cognitive functions such as learning, problem-solving, and decision-making. AI technologies can be classified into two main types: narrow or weak AI, which is designed for a particular task, and general or strong AI, which possesses the ability to understand, learn, and apply knowledge across various domains. One of the most popular approaches in AI is machine learning, where algorithms are trained on large datasets to recognize patterns and make predictions."

if __name__ == "__main__":
    while True:
        input_text = input("Enter the text for summarization (type 'exit' to end): ")

        if input_text.lower() == 'exit':
            print("Exiting...")
            break

        bert_model = Summarizer()

        summary = bert_model(input_text)
 
        print(summary)
