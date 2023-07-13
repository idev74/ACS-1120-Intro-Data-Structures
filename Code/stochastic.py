import sys
import random
import string
from histogram import histogram

source_text = "Code/corpus.txt"

def sample():
    words = histogram()
    word = random.choice(words)
    return word

def sentence():
    words = histogram()
    word = random.choice(words)
    sentence = word
    while word[-1] not in ".?!":
        word = random.choice(words)
        sentence += f"{word} "
    sentence.capitalize()
    return sentence

if __name__ == "__main__":
    print(sentence())




