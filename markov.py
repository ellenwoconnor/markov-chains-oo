import sys
from random import choice


class SimpleMarkovGenerator(object):

    def read_files(self, filenames):
        """Given a list of files, make chains from them."""

        input_text = open(filenames).read()
        return input_text

    def make_chains(self, corpus):
        """Takes input text as string; stores chains."""

        chains = {}

        words = corpus.split()

        for i in range(len(words) - 2):
            key = (words[i], words[i + 1])
            value = words[i + 2]

            if key not in chains:
                chains[key] = []

            chains[key].append(value)

            # or we could say "chains.setdefault(key, []).append(value)"

        return chains

    def make_text(self, chains):
        """Takes dictionary of markov chains; returns random text."""

        key = choice(chains.keys())
        words = [key[0], key[1]]
        while key in chains:
            # Keep looping until we have a key that isn't in the chains
            # (which would mean it was the end of our original text)
            #
            # Note that for long texts (like a full book), this might mean
            # it would run for a very long time.

            word = choice(chains[key])
            words.append(word)
            key = (key[1], word)

        print " ".join(words)

if __name__ == "__main__":

    input_path = sys.argv[1]
    new_markov = SimpleMarkovGenerator()
    input_text = new_markov.read_files(input_path)
    dictionary = new_markov.make_chains(input_text)
    text_generator1 = new_markov.make_text(dictionary)
    text_generator2 = new_markov.make_text(dictionary)  
    text_generator3 = new_markov.make_text(dictionary)
    text_generator4 = new_markov.make_text(dictionary)
    text_generator5 = new_markov.make_text(dictionary)
