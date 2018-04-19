import csv
import pickle
from stresses import *
from rhymes import *
from timeit import default_timer as timer
import nltk

entries = nltk.corpus.cmudict.dict()

#TODO: switch between csv and file based on extension

def readCSV(filename):
    with open(filename, newline='') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
        returnlist = [row for row in csvreader]
        return returnlist[0]

def readFile(filename):
    with open(filename, 'r') as f:
        returnlist = [line.strip().replace('_', ' ') for line in f]
        return returnlist

def buildStressesDict(wordList):
    stressesDict = {}
    timing_list = []
    stepthroughlistStart = timer()
    for i in wordList:
        currentStress = get_stress_of_phrase(i, entries)
        if '?' in currentStress:
            pass
        if currentStress in stressesDict:
            stressesDict[currentStress].append(i)
        else:
            stressesDict[currentStress] = [i]

    stepthroughlistEnd = timer()
    print('dictionary generated in ' + str(stepthroughlistEnd - stepthroughlistStart))
    return stressesDict

def buildRhymesDict(wordList):
    rhymesDict = {}
    timing_list = []
    stepthroughlistStart = timer()
    for i in wordList:
        currentRhyme = get_rhyme_of_phrase(i, entries)
        if '?' in currentRhyme:
            pass
        if currentRhyme in rhymesDict:
            rhymesDict[currentRhyme].append(i)
        else:
            rhymesDict[currentRhyme] = [i]

    stepthroughlistEnd = timer()
    print('dictionary generated in ' + str(stepthroughlistEnd - stepthroughlistStart))
    return rhymesDict

def createPickle(inputfile, outputfile):
    wordlist = readCSV(inputfile) if inputfile[-3:] == 'csv' else readFile(inputfile)
    stressesDict = buildStressesDict(wordlist)
    with open(outputfile, 'wb') as f:
        pickle.dump(stressesDict, f, pickle.HIGHEST_PROTOCOL)

def createRhymePickle(inputfile, outputfile):
    wordlist = readCSV(inputfile) if inputfile[-3:] == 'csv' else readFile(inputfile)
    rhymesDict = buildRhymesDict(wordlist)
    with open(outputfile, 'wb') as f:
        pickle.dump(rhymesDict, f, pickle.HIGHEST_PROTOCOL)

createPickle('../data/birdfile.csv', '../data/birds.pickle')
createRhymePickle('../data/birdfile.csv', '../data/birds-rhyme.pickle')
