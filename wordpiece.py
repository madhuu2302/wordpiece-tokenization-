from collections import Counter

words = {
    "cat": 3,
    "cats": 2,
    "dog": 1
}
print("========================================")
print("       WORDPIECE TOKENIZER")
print("========================================")
print("\nTraining words:")
print(words)

splits = {
    "cat": ["c", "##a", "##t"],
    "cats": ["c", "##a", "##t", "##s"],
    "dog": ["d", "##o", "##g"]
}
print("\nInitial splits:")
for word, tokens in splits.items():
    print(word, "->", tokens)
token_freq = Counter()
for word, freq in words.items():
    tokens = splits[word]
    for token in tokens:
        token_freq[token] += freq
print("\nToken frequencies:")
for token, freq in token_freq.items():
    print(token, "=", freq)
pair_freq = Counter()
for word, freq in words.items():
    tokens = splits[word]
    for i in range(len(tokens) - 1):
        pair = (tokens[i], tokens[i + 1])
        pair_freq[pair] += freq
print("\nPair frequencies:")
for pair, freq in pair_freq.items():
    print(pair, "=", freq)

scores = {}
for pair, freq in pair_freq.items():
    first = pair[0]
    second = pair[1]
    score = freq / (
        token_freq[first] * token_freq[second]
    )
    scores[pair] = score
print("\nWordPiece scores:")
for pair, score in scores.items():
    print(
        pair,
        "=",
        round(score, 4)
    )

best_pair = max(
    scores,
    key=scores.get
)
print("\nBest pair:")
print(best_pair)
print(
    "Best score:",
    round(scores[best_pair], 4)
)
def merge_pair(splits, pair):
    new_token = (
        pair[0]
        +
        pair[1].replace("##", "")
    )
    for word in splits:
        tokens = splits[word]
        new_tokens = []
        i = 0
        while i < len(tokens):
            if i < len(tokens) - 1:
                current_pair = (
                    tokens[i],
                    tokens[i + 1]
                )
                if current_pair == pair:
                    new_tokens.append(
                        new_token
                    )
                    i += 2
                    continue
            new_tokens.append(
                tokens[i]
            )
            i += 1
        splits[word] = new_tokens
    return new_token

new_token = merge_pair(
    splits,
    best_pair
)
print("\nNew token created:")
print(new_token)
print("\nUpdated splits:")

for word, tokens in splits.items():
    print(word, "->", tokens)


vocab = {
    "c",
    "d",
    "##a",
    "##t",
    "##s",
    "##o",
    "##g",
    "do"
}
print("\nVocabulary:")
print(vocab)
def tokenize_word(word, vocab):
    tokens = []
    while len(word) > 0:
        found = False

        for i in range(
            len(word),
            0,
            -1
        ):
            part = word[:i]
            if len(tokens) > 0:
                part = "##" + part
            if part in vocab:
                tokens.append(part)
                word = word[i:]
                found = True
                break
        if not found:
            return ["[UNK]"]
    return tokens

new_word = "dog"
tokens = tokenize_word(
    new_word,
    vocab
)
print("\nTokenization:")
print(new_word, "->", tokens)

vocab_ids = {
    "[UNK]": 0,
    "c": 1,
    "d": 2,
    "##a": 3,
    "##t": 4,
    "##s": 5,
    "##o": 6,
    "##g": 7,
    "do": 8
}

ids = []
for token in tokens:
    ids.append(
        vocab_ids[token]
    )
print("\nTokens:")
print(tokens)
print("\nToken IDs:")
print(ids)

unknown_word = "xyz"
unknown_tokens = tokenize_word(
    unknown_word,
    vocab
)
print("\nUnknown word test:")
print(
    unknown_word,
    "->",
    unknown_tokens
)
print("\n========================================")
print("             FINAL RESULT")
print("========================================")
print("Input word :", new_word)
print("Tokens     :", tokens)
print("Token IDs  :", ids)
print("\nWordPiece process completed!")