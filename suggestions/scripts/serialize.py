import sys
sys.path.insert(0, "..")
import pickle
from lib.trie import Trie


if __name__ == "__main__":
    corpus = Trie()

    with open("../src/corpus.txt", "r") as file:
        line = file.readline()
        while line:
            corpus.insert(line.rstrip().lower())
            line = file.readline()

    with open("../src/corpus.pickle", "wb") as file:
        pickle.dump(corpus, file, protocol=pickle.HIGHEST_PROTOCOL)
