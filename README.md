# Docker NLP

This project provides basic Python examples for various Natural Language Processing (NLP) tasks with Docker.

## Table of Contents
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)

## Getting Started

These instructions will help you get the project up and running on your local machine for development and testing purposes.

### Prerequisites

List any prerequisites or dependencies that need to be installed before can use the project.

- [Docker Desktop](https://www.docker.com/products/docker-desktop/)
- [Python](https://www.python.org/)

## Task Examples:

1. **[Sentiment Analysis](#sentiment-analysis):** Process of analyzing digital text to determine if the emotional tone of the message is positive, negative, or neutral.

2. **[Named Entity Recognition](#named-entity-recognition):** Identify entities (e.g., persons, organizations, locations) in a given sentence.

3. **[Text Classification](#text-classification):** Predict the category or class of a given piece of text.

4. **[Text Summarization](#text-summarization):** Generate a summarized version of a longer piece of text (e.g., an article).

5. **[Text Translation](#text-translation):** Translate a sentence from one language to another.

## Usage with Docker :
   
1. Pull Docker image
   ```sh
   docker pull harshmanvar/basic-nlp:v1
   ```

2. Run Docker image
   ```sh
   docker run -it harshmanvar/basic-nlp:v1 <file-name.py>
   ```
-  **Sentiment Analysis Example** :

   ```sh
   docker run -it harshmanvar/basic-nlp:v1 01_sentiment_analysis.py
   ```

   Enter your input

   ```
   Enter the text for semantic analysis (type 'exit' to end): Docker is very cool tool..!
   Sentiment: Positive

   Enter the text for semantic analysis (type 'exit' to end): John is Idiot
   Sentiment: Negative

   Enter the text for semantic analysis (type 'exit' to end): Elephant
   Sentiment: Neutral
   ```

## Installation:

1. **Clone the repository**
   ```sh
   git clone https://github.com/harsh4870/Docker-NLP.git
   ```

2. **Install dependencies & Virtual env**
   ```sh
   python3 -m venv venv && pip install -r requirements.txt && source venv/bin/activate
   ```

3. **Run Examples:**
   
   Choose the specific task you want to run:

     ```bash
     python 01_sentiment_analysis.py
     python 02_name_entity_recognition.py
     python 03_text_classification.py
     python 04_text_summarization.py
     python 05_language_translation.py
     ```

## Task Examples:

### **Sentiment Analysis** :

   ```sh
   docker run -it harshmanvar/basic-nlp:v1 01_sentiment_analysis.py
   ```

   Enter your input

   ```
   Enter the text for semantic analysis (type 'exit' to end): Docker is very cool tool..!
   Sentiment: Positive

   Enter the text for semantic analysis (type 'exit' to end): John is Idiot
   Sentiment: Negative

   Enter the text for semantic analysis (type 'exit' to end): Elephant
   Sentiment: Neutral
   ```

### **Named Entity Recognition** :

   ```sh
   docker run -it harshmanvar/basic-nlp:v1 02_name_entity_recognition.py
   ```

   Enter your input

   ```
   Enter the text for entity recognition (type 'exit' to end): Apple Inc. is planning to open a new store in San Francisco. Tim Cook is the CEO of Apple. 
   
   Entity: Apple Inc., Type: ORG
   Entity: San Francisco, Type: GPE
   Entity: Tim Cook, Type: PERSON
   Entity: Apple, Type: ORG
   ```

### **Text Classification** :

   ```sh
   docker run -it harshmanvar/basic-nlp:v1 03_text_classification.py
   ```

   Enter your input

   ```
   Enter the text for classification (type 'exit' to end): Product is very Good
   Accuracy: 1.00
   Test Text (Positive): 'Product is very Good'
   Predicted Sentiment: Positive
 
   Enter the text for classification (type 'exit' to end): Product is not that good as per reviews
   Accuracy: 1.00
   Test Text (Positive): 'Product is not that good as per reviews'
   Predicted Sentiment: Negative
   ```

### **Text Summarization** :

   ```sh
   docker run -it harshmanvar/basic-nlp:v1 04_text_summarization.py
   ```

   Enter your input

   ```
   Enter the text for summarization (type 'exit' to end): Artificial intelligence (AI) is a branch of computer science that aims to create machines capable of intelligent behavior. These machines are designed to mimic human cognitive functions such as learning, problem-solving, and decision-making. AI technologies can be classified into two main types: narrow or weak AI, which is designed for a particular task, and general or strong AI, which possesses the ability to understand, learn, and apply knowledge across various domains. One of the most popular approaches in AI is machine learning, where algorithms are trained on large datasets to recognize patterns and make predictions.                       

   Artificial intelligence (AI) is a branch of computer science that aims to create machines capable of intelligent behavior. These machines are designed to mimic human cognitive functions such as learning, problem-solving, and decision-making.
   ```

### **Text Translation** :

   ```sh
   docker run -it harshmanvar/basic-nlp:v1 05_language_translation.py
   ```

   Enter your input

   ```
   Enter the text for translation (type 'exit' to end): Hello, how are you doing?
   Original Text: Hello, how are you doing?
   Translated Text: Bonjour comment allez-vous?
   ```