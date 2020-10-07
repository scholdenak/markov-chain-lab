"""Generate Markov text from text files."""

from random import choice


def open_and_read_file(file_path):
    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    # your code goes here
    
    text_string = open(file_path).read()
        
    #opens the file

    return text_string

    #return 'Contents of your file as one long string'


def make_chains(text_string):
    """Take input text as string; return dictionary of Markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> chains = make_chains('hi there mary hi there juanita')

    Each bigram (except the last) will be a key in chains:

        >>> sorted(chains.keys())
        [('hi', 'there'), ('mary', 'hi'), ('there', 'mary')]

    Each item in chains is a list of all possible following words:

        >>> chains[('hi', 'there')]
        ['mary', 'juanita']

        >>> chains[('there','juanita')]
        [None]
    """

    chains = {}

    # your code goes here
    markov_words = text_string.split()
    # markov_list = []
    for i in range(len(markov_words) - 2 ):
        # markov_list.extend(markov_words[i], markov_words[i+1])
        markov_tuples = tuple((markov_words[i], markov_words[i+1]))
        # markov_list = markov_list + markov_tuples
        # markov_list.append(markov_tuples)
        word_list = markov_words[i + 2]            
            
        if tuple_key not in chains:
            chains[tuple_key] = []
        chains[tuple_key].append(word_list)
            
#  for i in range(len(words) - 2):
#         key = (words[i], words[i + 1])
#         value = words[i + 2]

#         if key not in chains:
#             chains[key] = []

#         chains[key].append(value)


            
#             for tuple_key, value in chains:
#                 (list(value).append(markov_words[i]))
#             # 
            #     chains[tuple_key] = [chains[tuple_key] + (markov_words[i + 2])]
            # if tuple_key in chains:
            #     chains[tuple_key] = add to dict(chains.get(tuple_key, markov_words[i + 2])
                # chains[tuple_key] = markov_words[i + 2]
        # append dict {(tuple):[markov_words[i + 2]]}
        # for key in markov_tuples:
        # if key not in chains:
        #     # append dict {(tuple):[markov_words[i + 2]]
        # if key is in chains:
            # go to key (append the list)

        # for key in markov_tuples:
        #     chains[key] = chains.get(key, markov_words[i + 2])

        # else 

        
        
        
    print(chains)

    # create tuple  from markov words[i] and markov_words[i + 1]

    # return chains


def make_text(chains):
    """Return text from chains."""

    words = []

    # your code goes here

    return ' '.join(words)


input_path = 'green-eggs.txt'

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text)

# Produce random text
random_text = make_text(chains)

print(random_text)
