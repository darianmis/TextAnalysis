import re
from collections import Counter
import matplotlib.pyplot as plt

def read_file(path):
    with open(path, 'r', encoding='utf-8') as file:
        return file.read()

def tokenize(text):
    return re.findall(r'\b\w+\b', text.lower())

def word_counts(words):
    return Counter(words)

def split_sentences(text):
    return re.split(r'(?<=[.!?])\s+', text.strip())

def sentence_lengths(text):
    sentences = split_sentences(text)
    return [len(tokenize(sentence)) for sentence in sentences]


def plot_visuals(counter, lengths, n=10):
    plt.figure(figsize=(12, 5))
    # Bar chart of top words
    plt.subplot(1, 2, 1)
    top = counter.most_common(n)
    words, counts = zip(*top) if top else ([], [])
    plt.bar(words, counts)
    plt.xticks(rotation=45, ha="right")
    plt.title("Top words")
    # Histogram of sentence lengths
    plt.subplot(1, 2, 2)
    plt.hist(lengths, bins=20)
    plt.title("Sentence length distribution (words)")
    plt.xlabel("Words per sentence")
    plt.ylabel("Frequency")
    avg_length = sum(lengths) / len(lengths) if lengths else 0
    plt.figtext(0.5, 0.01, f"Average sentence length: {avg_length:.2f} words", ha="center")
    plt.tight_layout()
    plt.show()

def ngrams(tokens, n):
    return list(zip(*(tokens[i:] for i in range(n))))

def type_token_ratio(words):
    return len(set(words)) / len(words) if words else 0.0

if __name__ == "__main__":
    import os
    base_dir = os.path.dirname(os.path.abspath(__file__))
    text_path = os.path.join(base_dir, "text.txt")
    text = read_file(text_path)
    words = tokenize(text)
    counts = word_counts(words)
    for word, count in counts.most_common(10):
        print(f"{word}: {count}")
    lengths = sentence_lengths(text)
    avg_length = sum(lengths) / len(lengths) if lengths else 0
    print(f"Average sentence length: {avg_length:.2f} words")
    plot_visuals(counts, lengths, n=10)
    ttr = type_token_ratio(words)
    print(f"Type-Token Ratio: {ttr:.3f}")
    bigrams = Counter(ngrams(words, 2))
    trigrams = Counter(ngrams(words, 3))
    print("Top 5 Bigrams:")
    for bg, count in bigrams.most_common(5):
        print(f"{' '.join(bg)}: {count}")
    print("Top 5 Trigrams:")
    for tg, count in trigrams.most_common(5):
        print(f"{' '.join(tg)}: {count}")
