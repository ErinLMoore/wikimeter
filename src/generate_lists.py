from find_matches import *


test_phrase = 'eleanor rigby'
stresses_list = find_matches_from_pickle('../data/birds.pickle',test_phrase)
rhymes_list =find_rhyme_matches_from_pickle('../data/birds-rhyme.pickle',test_phrase)
intersection_list = set(stresses_list).intersection(rhymes_list)
[print(i) for i in intersection_list ]

#madagascan serpent eagle
#Rodrigues solitaire
