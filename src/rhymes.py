from itertools import chain

# entries = nltk.corpus.cmudict.dict()

def get_pron(word, entries):
    findword = word.lower()
    if findword in entries:
        mypron =  entries[findword]
    else:
        mypron = ['?']
    return mypron[0]

def get_rhyme_of_phrase(phraseString, entries):
    phraseString = phraseString.replace('-', ' ')
    phraseList = phraseString.split(' ')
    alist = [get_pron(word, entries) for word in phraseList]
    flattened = list(chain.from_iterable([get_pron(word, entries) for word in phraseList]))
    returnlist = flattened[-2:] if len(flattened) > 2 else flattened
    return (',').join(returnlist)
