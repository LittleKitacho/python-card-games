from random import randint

class deck:
    def __init__(type): # Assign Deck
        if type == None:
            raise ValueError('\'type\' is not defined!')
        if type == 0 # Regular Deck
            if verbose = True:
                print('Normal deck assigned, returning.')
            return shuffle(['C1','C2','C3','C4','C5','C6','C7','C8','C9','C10','C11','C12','C13','D1','D2','D3','D4','D5','D6','D7','D8','D9','D10','D11','D12','D13','H1','H2','H3','H4','H5','H6','H7','H8','H9','H10','H11','H12','H13','S1','S2','S3','S4','S5','S6','S7','S8','S9','S10','S11','S12','S13'])
        elif type == 1: # Number-Only Deck
            if verbose = True:
                print('Number-Only deck assigned, returning.')
            return shuffle(['1','2','3','4','5','6','7','8','9','10','11','12','13','1','2','3','4','5','6','7','8','9','10','11','12','13','1','2','3','4','5','6','7','8','9','10','11','12','13','1','2','3','4','5','6','7','8','9','10','11','12','13'])
        elif type == 3: # Regular Deck w/Jokers
            return shuffle(['C1','C2','C3','C4','C5','C6','C7','C8','C9','C10','C11','C12','C13','D1','D2','D3','D4','D5','D6','D7','D8','D9','D10','D11','D12','D13','H1','H2','H3','H4','H5','H6','H7','H8','H9','H10','H11','H12','H13','S1','S2','S3','S4','S5','S6','S7','S8','S9','S10','S11','S12','S13','J','J'])
        elif type == 4: # Number-Only Deck w/Jokers
            return shuffle(['1','2','3','4','5','6','7','8','9','10','11','12','13','1','2','3','4','5','6','7','8','9','10','11','12','13','1','2','3','4','5','6','7','8','9','10','11','12','13','1','2','3','4','5','6','7','8','9','10','11','12','13','J','J'])
    def shuffle(deckIn):
        if !type(deckIn) in (tuple, list):
            raise ValueError('\'deck\' is not a list or tuple!')
        take = 0, deckOut = []
        while deckOut.len <= deckIn.len:
            take = randint(1, deckIn.len)
            if not deckIn[take] == 0:
                deckOut.append(deckIn(take))
                deckIn[take] = 0
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