import random
import pickle
import nltk
from stresses import *
from rhymes import *

entries = nltk.corpus.cmudict.dict()


def find_stress_matches(phrase, stress_dict, entries = entries):
    phrase_stress = get_stress_of_phrase(phrase, entries)
    if phrase_stress in stress_dict:
        return(stress_dict[phrase_stress])
    else:
        return(['no matches found'])

def find_random_stress_match(phrase, stress_dict):
    return random.choice(find_matches(phrase, stress_dict))


def find_matches_from_pickle(picklefile, word):
    with open(picklefile, 'rb') as f:
        stresses_dict = pickle.load(f)
    return(find_stress_matches(word, stresses_dict))

def find_random_match_from_pickle(picklefile, word):
    with open(picklefile, 'rb') as f:
        stresses_dict = pickle.load(f)
    return(find_random_stress_match(word, stresses_dict))

#####################################################


def find_rhyme_matches(phrase, rhyme_dict, entries = entries):
    phrase_rhyme = get_rhyme_of_phrase(phrase, entries)
    if phrase_rhyme in rhyme_dict:
        return(rhyme_dict[phrase_rhyme])
    else:
        return(['no matches found'])

def find_random_rhyme_match(phrase, rhyme_dict):
    return random.choice(find_rhyme_matches(phrase, rhyme_dict))

def find_rhyme_matches_from_pickle(picklefile, word):
    with open(picklefile, 'rb') as f:
        rhymes_dict = pickle.load(f)
    return(find_rhyme_matches(word, rhymes_dict))

def find_random_rhyme_match_from_pickle(picklefile, word):
    with open(picklefile, 'rb') as f:
        rhymes_dict = pickle.load(f)
    return(find_random_rhyme_match(word, rhymes_dict))
