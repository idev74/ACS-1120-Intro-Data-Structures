import random
import sys

def rearrange():
    sentence = sys.argv[1:]
    random.shuffle(sentence)
    rearranged = " ".join(sentence)
    print(rearranged)

rearrange()