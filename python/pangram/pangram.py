import string

def is_pangram(sentence):
    sentence = sentence.lower()  # Convert the sentence to lowercase

    alphabet = set(string.ascii_lowercase)  # Set of all lowercase letters

    # Check if the set of letters in the sentence contains all the letters in the alphabet
    return alphabet.issubset(set(sentence))
