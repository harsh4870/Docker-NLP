import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
from sklearn.metrics import accuracy_score, classification_report
from sklearn.model_selection import train_test_split
import ssl

try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    pass
else:
    ssl._create_default_https_context = _create_unverified_https_context
nltk.download('vader_lexicon')

# Text data
texts = [
    "This is a very good product. Very much liked it.",
    "This is a terrible product. I'm very disappointed.",
    "Spam message: win a prize!",
    "I absolutely love this new feature! It's fantastic.",
    "Worst experience ever. I regret buying this.",
    "Get 50% off on our latest products! Limited time offer!",
]

# Labels: 0 for positive, 1 for negative, 2 for spam
labels = [0, 1, 2, 0, 1, 2]

X_train, X_test, y_train, y_test = train_test_split(texts, labels, test_size=0.2, random_state=42)

sia = SentimentIntensityAnalyzer()
vader_predictions = [sia.polarity_scores(text)["compound"] for text in X_test]
threshold = 0.2
vader_classifications = [0 if score > threshold else 1 for score in vader_predictions]
accuracy = accuracy_score(y_test, vader_classifications)
report_vader = classification_report(y_test, vader_classifications, zero_division='warn')

# Sample text
# test_text_positive = "I'm so excited about the new update! It's amazing!"
# test_text_negative = "This is a total disaster. I can't believe I wasted money on this."

if __name__ == "__main__":
    while True:
        input_text = input("Enter the text for classification (type 'exit' to end): ")

        if input_text.lower() == 'exit':
            print("Exiting...")
            break

        input_text_score = sia.polarity_scores(input_text)["compound"]
        input_text_classification = 0 if input_text_score > threshold else 1

        print(f"Accuracy: {accuracy:.2f}")
        print("\nVADER Classification Report:")
        print(report_vader)

        print(f"\nTest Text (Positive): '{input_text}'")
        print(f"Predicted Sentiment: {'Positive' if input_text_classification == 0 else 'Negative'}")

