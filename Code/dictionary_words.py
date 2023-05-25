import random
import sys

def random_sentence():
    length = int(sys.argv[1])
    file = open("/usr/share/dict/words", "r")
    words = file.read().split()
    random_words = random.sample(words, length)
    random_words[-1] = random_words[-1] + "."
    random_words[0] = random_words[0].capitalize()
    file.close()
    return " ".join(random_words)

if __name__ == "__main__":
    print(random_sentence())
    