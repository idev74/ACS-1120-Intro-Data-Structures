import string

def histogram():
    source_text = open("Code/corpus.txt", "r").read().split()
    return source_text

def unique_words():
    histogram = histogram()
    unique_words = []
    for word in histogram:
        word = word.translate(str.maketrans('', '', string.punctuation))
        if word not in unique_words:
            unique_words.append(word)
    return unique_words

def frequency():
    frequency = {}
    for word in histogram():
        word = word.translate(str.maketrans('', '', string.punctuation))
        frequency[word] = 1 if word not in frequency else frequency[word] + 1
    return frequency

if __name__ == "__main__":
    print(frequency())
