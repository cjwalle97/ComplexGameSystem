class Goal (object):
    '''Desired end result of Gentic Algorithm'''
    def __init__(self, goal):
        self.goal = goal
        letterlist = []
        for i in goal:
            self.letters += 1
            letterlist.append[i]

class Chromosome (object):
    '''list of characters that must match up to Goal's LetterList'''
    def __init__(self, fit)
        fitness = fit

class Generation(object):
    '''Contains a list of 10 chromosomes that will be crossbred and mutated to form new chromosomes'''

def Evaluation(chromosome, goal):
    '''Checks the current chromosome to determine fitness based off the goal'''

def Crossover():
    '''Swaps parts of one chromosome with another in order to try and form a more fit chromosome '''
    
def Mutation():
    '''Randomly changes parts of a Chromosome in order to try make it more fit.'''

def Evolution():
    '''Calls the Evaluation, Crossover, and Mutation Functions in order to create a new Generation that will hopefully be more fit than the last one'''
