WordPiece Tokenization
A from-scratch implementation of the WordPiece Tokenization algorithm using Python. This project demonstrates the basic workflow of WordPiece tokenization, including character-level splitting, token frequency calculation, pair frequency calculation, WordPiece score calculation, subword pair merging, vocabulary construction, tokenization, and token-to-ID conversion.

Overview
WordPiece is a subword tokenization technique widely used in Natural Language Processing (NLP). Instead of representing every word as a single token, WordPiece divides words into smaller subword units.

For example:

played → play + ##ed

The ## prefix indicates that the subword is a continuation of the previous token.

This project provides a simple from-scratch implementation to demonstrate how WordPiece tokenization works from training data to final token IDs.

Features

Training word frequency representation
Initial character-level token splitting
Token frequency calculation
Pair frequency calculation
WordPiece score calculation
Best pair selection
Subword pair merging
Vocabulary construction
Greedy longest-match tokenization
Token-to-ID conversion
Unknown word handling using [UNK]


Technologies Used

Python
Collections Counter
Natural Language Processing (NLP) concepts

Project Workflow

Training Data
↓
Initial Character Splits
↓
Token Frequencies
↓
Pair Frequencies
↓
WordPiece Score Calculation
↓
Best Pair Selection
↓
Subword Pair Merging
↓
Vocabulary Creation
↓
New Word Tokenization
↓
Token-to-ID Conversion
↓
Unknown Word Handling

Training Data

The implementation uses a small sample vocabulary:
words = {
    "cat": 3,
    "cats": 2,
    "dog": 1
}

Initial Splits

Each word is initially divided into character-level subword tokens.

cat  → c + ##a + ##t
cats → c + ##a + ##t + ##s
dog  → d + ##o + ##g

The first character is represented normally, while subsequent characters use the ## prefix to indicate continuation tokens.

Token Frequencies

The frequency of each token is calculated based on the frequency of the corresponding training words.

For the given training data, the token frequencies include:

c = 5
##a = 5
##t = 5
##s = 2
d = 1
##o = 1
##g = 1
Pair Frequencies

Adjacent token pairs are identified and their frequencies are calculated.

For example, the word dog contains the pairs:

(d, ##o)
(##o, ##g)

The pair frequency is calculated using the frequency of the training word in which the pair occurs.

WordPiece Scoring

For every adjacent token pair, a WordPiece score is calculated using the following formula:

Score = Pair Frequency / (Frequency of First Token × Frequency of Second Token)

The pair with the highest score is selected as the best candidate for merging.

This scoring process helps determine which subword pair should be combined to create a new vocabulary token.

Best Pair Selection

After calculating the scores for all adjacent token pairs, the pair with the highest WordPiece score is selected.

The selected pair is then passed to the merging process.

Pair Merging

The selected token pair is merged to create a new subword token.

For example:

d + ##o → do

After merging, the tokenization of the corresponding word becomes:

dog → do + ##g

The newly created token is then added to the vocabulary.

Vocabulary

The project creates a vocabulary containing the original subword tokens and the newly generated token.

Example vocabulary:

c
d
##a
##t
##s
##o
##g
do

An [UNK] token is also used during tokenization to represent unknown words.

Tokenization

The tokenizer uses a greedy longest-match approach.

For a new word, the tokenizer searches for the longest subword available in the vocabulary. If a matching subword is found, it is added to the token list and the remaining part of the word is processed.

For example:

Input:
dog

Output:
['do', '##g']

The tokenizer continues this process until the complete word has been represented.

Token IDs

After tokenization, each token is converted into a numerical ID using the vocabulary-to-ID mapping.

Example:

Tokens:
['do', '##g']

Token IDs:
[8, 7]

Token IDs allow text to be represented numerically so that it can be processed by Natural Language Processing and machine learning systems.

Unknown Word Handling

The implementation also tests an unknown word:

xyz → ['[UNK]']

[UNK] represents an unknown token that cannot be completely represented using the available vocabulary.

Sample Output
========================================
       WORDPIECE TOKENIZER
========================================

Training words:
{'cat': 3, 'cats': 2, 'dog': 1}

Initial splits:
cat -> ['c', '##a', '##t']
cats -> ['c', '##a', '##t', '##s']
dog -> ['d', '##o', '##g']

Token frequencies:
c = 5
##a = 5
##t = 5
##s = 2
d = 1
##o = 1
##g = 1

WordPiece scores:
...

Best pair:
('d', '##o')

New token created:
do

Updated splits:
dog -> ['do', '##g']

Tokenization:
dog -> ['do', '##g']

Tokens:
['do', '##g']

Token IDs:
[8, 7]

Unknown word test:
xyz -> ['[UNK]']

========================================
             FINAL RESULT
========================================

Input word : dog
Tokens     : ['do', '##g']
Token IDs  : [8, 7]

WordPiece process completed!
Learning Outcomes

This project demonstrates the following concepts:

Subword tokenization
Character-level token splitting
Vocabulary construction
Token frequency calculation
Pair frequency calculation
WordPiece scoring
Subword pair merging
Greedy longest-match tokenization
Token-to-ID conversion
Unknown token handling
Applications

WordPiece Tokenization is useful in various Natural Language Processing applications, including:

Text Classification
Sentiment Analysis
Question Answering
Language Models
Transformer-based NLP systems
Text Representation
Project Structure
WordPiece-Tokenization/
│
├── Word piece.py
└── README.md
How to Run
1. Clone the Repository
git clone https://github.com/YOUR-USERNAME/WordPiece-Tokenization.git
2. Open the Project Directory
cd WordPiece-Tokenization
3. Run the Python Program

Since the Python file contains spaces in its name, use:

python "Word piece.py"

Alternatively, on systems using the Python launcher:

py "Word piece.py"
Requirements

This project uses Python's built-in collections module. No external Python packages are required.

The project can be executed using Python 3.x.

Conclusion

This project provides a simple from-scratch implementation of WordPiece Tokenization using Python. It demonstrates the complete basic process of calculating token and pair frequencies, calculating WordPiece scores, selecting the best pair, merging subwords, constructing a vocabulary, tokenizing new words, and converting tokens into numerical IDs.

The implementation provides a practical understanding of how subword tokenization works and how it can be used as a fundamental component of Natural Language Processing systems.

AUTHOR

Madhumitha
