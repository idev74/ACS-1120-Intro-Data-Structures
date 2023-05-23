import random

def read_words():
    file = open("/usr/share/dict/words", "r")
    words = file.read().splitlines()
    random_word = random.choice(words)
    file.close()
    return random_word

def random_sentence():
    sentence = []
    for i in range(0, 10):
        sentence.append(read_words())
    return " ".join(sentence)


    
if __name__ == "__main__":
    print(random_sentence())
    

