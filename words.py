#1
for word in ['hi', 'bye', 'pressure', 'everest']: 
    print(word.upper())

#2
def print_upper_words(words):
    """For a list of words, print out each word, but in all uppercase"""

    for word in words: 
        print(word.upper())

print_upper_words(['hi', 'bye', 'pressure', 'everest'])

#3
def print_upper_words(words):
    """For a list of words, print out each word beginning with 'e', but in all uppercase"""

    for word in words:
        if word[0] == 'e': 
            print(word.upper())

print_upper_words(['hi', 'bye', 'pressure', 'everest'])

#4
def print_upper_words(words, must_start_with):
    """For a list of words, print out each word beginning with specified letter, but in all uppercase"""

    for word in words:
        for char in must_start_with:
            if word[0] == char: 
                print(word.upper())

print_upper_words(['hi', 'bye', 'pressure', 'everest'], ['h', 'p'])