def break_word(stuff):
    """ This function will break up words."""
    words = stuff.split(' ')
    return words

def sort_word(words):
    """ sort the words. """
    return sorted(words)

def print_first_word(words):
    """ print the first word after popping it off."""
    word = words.pop(0)
    print word

def print_last_word(words):
    """ print the last word after popping it off."""
    word = words.pop(-1)
    print word

def sort_sentence(sentence):
    """ takes in a full sentence and returns the sorted words. """
    word = break_word(sentence)
    return sort_word(word)

def print_first_and_last(sentence):
    """ print the first and last words of the sentence. """
    word = break_word(sentence)
    print_first_word(word)
    print_last_word(word)

def print_first_and_last_sorted(sentence):
    """ sort the words and then print the first and last one. """
    word = sort_sentence(sentence)
    print_first_word(word)
    print_last_word(word)

