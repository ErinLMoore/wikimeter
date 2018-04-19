from itertools import chain

def get_stress(word, entries):
    findword = word.lower()
    if findword in entries:
        mypron =  entries[findword]
        mystress = [char for phone in mypron[0] for char in phone if char.isdigit()]
    else:
        mystress = ['?']
    return mystress

def get_stress_of_phrase(phraseString, entries):
    phraseString = phraseString.replace('-', ' ')
    phraseList = phraseString.split(' ')
    flattened = list(chain.from_iterable([get_stress(word, entries) for word in phraseList]))
    return (',').join(flattened)
