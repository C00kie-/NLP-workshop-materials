## What is Text preprocessing?

In order to get started with NLP we need to understand text processing. As many may know, a lot of data in cybersecurity is unstructured and raw, it can’t be used straight away and needs pre-processing. In NLP, we take this unstructured text data as input and transform it into a format that computers can understand.

### Tokenization

Tokenization is breaking down a sentence into individual words or tokens. There are many ways to do it. For example, consider the sentence “Hello, world!” (Hello programmers). If we simply split on spaces, we’d get [“Hello,”, “world!”, “!”]. But that might not be what we want – we might want to remove punctuation marks and treat “Hello,” as a single token. In NLP, we use techniques like word-based tokenization or regular expression (regex) based tokenization, among other, to achieve this.

### Stopwords


As you start working with text data, you’ll quickly realize that some words are more important than others. By opposition, the unimportant words are called stopwords. Stopwords are common words like “the”, “and”, “a”, etc., that don’t add much value to the meaning of the sentence (to keep it simple). In fact, they can actually make it harder for machines to understand the text! For instance, if we’re building a chatbot that responds to user queries, removing stopwords can help us focus on more meaningful words and improve our response accuracy.

### Stemming and Lemmatization


Stemming is about working with the root of a word. It’s like reducing words to their base form – it helps us group similar words together and make our text processing more efficient! Stemming involves removing suffixes like “-ed” or “-ing”, while lemmatization takes it a step further by reducing words to their dictionary form. Using the same example, “running” would become “run”, but “runs” would also become “run”. Using stemming or lemmatization or not is a choice, it depends on the results you want to obtain.
A text pre-processing example


Let’s walk through an example of text processing step-by-step. Imagine we’re building a chatbot that responds to user queries like “What is the weather like today?” We want to extract the main keywords from this sentence, so we can respond accordingly. First, we tokenize the sentence into individual words: [“What”, “is”, “the”, “weather”, “like”, “today”, “?”]. Next, we remove stopwords like “the” and “is” because they don’t add much value to our response. Then, we stem or lemmatize the remaining words to get their base form: [“what”, “weather”, “like”, “today”]. We might even remove the word “like” which comports several meaning depending contexts. Simply put, we will be able to process these words to determine how to respond to the user’s query.
