WordPiece Tokenizer 

WordPiece is a subword tokenization algorithm used by BERT-family models. It splits words into smaller subword tokens and uses a scoring method to select token pairs for merging.

In this project, the training words are:

cat  → 3
cats → 2
dog  → 1

Features

Creates initial character-level tokens
Uses ## for tokens occurring inside words
Calculates token frequencies
Calculates pair frequencies
Calculates WordPiece scores
Finds the highest-scoring pair
Merges token pairs
Tokenizes new words using the longest matching subword
Converts tokens into token IDs
Handles unknown words using

Technologies Used

Python
collections.Counter

Project Structure
wordpiece_tokenizer/
│
└── wordpiece.py
How It Works
1. Training Data
cat  → 3
cats → 2
dog  → 1
2. Initial Tokenization
cat  → c ##a ##t
cats → c ##a ##t ##s
dog  → d ##o ##g

The first character does not use ##; tokens occurring inside a word use ##.

3. Token Frequency

The program counts how frequently each individual token occurs.

4. Pair Frequency

Adjacent token pairs are counted, for example:

c + ##a
##a + ##t
d + ##o
##o + ##g
5. WordPiece Score

The program calculates a score for every pair using:

score = pair frequency /
        (first token frequency × second token frequency)

The highest-scoring pair is selected for merging.

6. Merge

The selected pair is combined into a new token.

For example:

d + ##o

becomes:

do
7. Tokenize a New Word

For example:

dog

can become:

["do", "##g"]

WordPiece searches for the longest available subword and then processes the remaining part.

8. Token IDs

Tokens are assigned numerical IDs.

Example:

["do", "##g"]

becomes:

[8, 7]
9. Unknown Words

If a word cannot be completely represented using the vocabulary, the tokenizer returns:

["[UNK]"]

Installation

No installation is required apart from Python.

Check Python:

python --version
Run the Project

Open the terminal inside the project folder:

python wordpiece.py

If python does not work on Windows, try:

py wordpiece.py

Output:<img width="1062" height="927" alt="Output 1" src="https://github.com/user-attachments/assets/52246d36-69f0-413a-89c0-e7b9d3b6efd8" />

Complete Pipeline

Training Data
      ↓
Initial Character Splits
      ↓
Token Frequencies
      ↓
Pair Frequencies
      ↓
WordPiece Scores
      ↓
Highest-Scoring Pair
      ↓
Merge Pair
      ↓
Updated Vocabulary
      ↓
Tokenize New Word
      ↓
Convert Tokens to IDs
      ↓
[UNK] for Unknown Words

👩‍💻 Author

Madhumitha.U
