 WordPiece Tokenization

 Overview

This project demonstrates the basic working of **WordPiece Tokenization using Python**.

WordPiece is a subword tokenization method commonly used in Natural Language Processing (NLP) and Transformer-based language models. It divides words into smaller subword tokens instead of treating every complete word as a single token.

This project implements the main steps of WordPiece Tokenization from scratch using a small training corpus.

Corpus

The training corpus used in this project contains the following words with their frequencies:

```text
cat   → 3
cats  → 2
dog   → 1

These words are used to demonstrate token frequency calculation, pair frequency calculation, WordPiece scoring, pair merging, and tokenization.

Initial Splits

The words are initially divided into character-level tokens.
cat   → c ##a ##t
cats  → c ##a ##t ##s
dog   → d ##o ##g

The ## symbol indicates that the token occurs inside a word.

Features

Creates initial character-level token splits
Uses ## for subword tokens
Calculates token frequencies
Calculates pair frequencies
Calculates WordPiece scores
Finds the best-scoring pair
Merges the selected pair
Creates a vocabulary
Tokenizes a new word
Converts tokens into token IDs
Handles unknown words using [UNK]

WordPiece Scoring

The WordPiece score is calculated using the following formula:
Score(pair) = Pair Frequency /
              (Frequency of First Token × Frequency of Second Token)

The program calculates the score for every adjacent token pair and selects the pair with the highest score.

Pair Merging

After finding the best pair, the program merges the two tokens into a new token.

The merge_pair() function checks each word and replaces the selected adjacent pair with the newly created token.

def merge_pair(splits, pair):
