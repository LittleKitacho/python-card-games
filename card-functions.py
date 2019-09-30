disclaimer = "Yes, you can use this card function package for yourself.  No, you may not market it as your own, that should be common sense.  Use it in any way you please."
print(disclaimer)

defaultDeck = 0
verbose = False

from random import randint

class deck:
    def __init__(type): # Assign Deck
        if type == None:
            type = defaultDeck
        if type == 0 # Regular Deck
            if verbose = True:
                print('Normal deck assigned, returning.')
            return shuffle([])
        elif type == 1: # Number-Only Deck
            if verbose = True:
                print('Number-Only deck assigned, returning.')
            return shuffle([1,2,3,4,5,6,7,8,9,10,11,12,13,1,2,3,4,5,6,7,8,9,10,11,12,13,1,2,3,4,5,6,7,8,9,10,11,12,13,1,2,3,4,5,6,7,8,9,10,11,12,13])
        elif type == 3: # Regular Deck w/Jokers
            if verbose == True:
                print('')
    def shuffle(deckIn):
        if !type(deckIn) in (tuple, list):
            raise ValueError('\'deck\' is not a list or tuple!')
        shuffleControl = 0, deckOut = []
        while deckOut.len <= deckIn.len
            
        return deckOut


class player:
    def __init__(name, deck, cards):
        if !type(name) in str:
            raise ValueError('\'name\' is not a string!')
        if !type(deck) in (tuple, list):
            raise ValueError('\'deck\' is not a list or tuple!')
        if !type(cards) in int:
            raise ValueError('\'cards\' is not an integer!')
        hand = [], deckOut = []
        while x >= cards:
            hand.append(deck[1])
            x ++
        deckOut.append(name, hand)
        return deckOut

class settings:
    def __init__:
        print('Default deck type: '+ defaultDeck)
        print('Verbose? '+ verbose)
    def verbose(change):
        if change == True:
            verbose = True
            print('card-functions verbose mode enabled.')
        elif change == False:
            verbose = change
        else:
            verbose = !verbose
            if verbose == True:
                print('card-functions verbose mode enabled.')
    def defaultDeck(change):
        if defaultDeck == None:
            raise ValueError('\'change\' must be an integer!')
        elif: change > 
        else:
            defaultDeck = change
            if verbose == True:
                print('defaultDeck changed to '+ defaultDeck)