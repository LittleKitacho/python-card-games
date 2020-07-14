class Card():
    '''Basic class for a card.

    Contains variables used for rendering cards and dealing with card game logic,
    DO NOT CHANGE!
    '''
    def __init__(self, id: int):
        '''Creates card using an ID.

        See about-cardfunctions.md for information about creating cards.

        Creating a deck automatically creates cards, so you shouldn't have to create more
        (unless you are using them as a display).
        '''
        self.id = id # 
        self.data = {}
        if id <= 1:
            if id = 0:
                self.data.suit = 4
                self.data.color = 0
                self.data.number = 0

    def flip(self):
        '''Flips a card.

        Can also be done by toggling the 'card.data.visible', but is not recommended.

        Doesn't work if not called from a card object.
        '''

class Deck():
    def __init__(self, **kwargs):
        jokers = kwargs.get("jokers", False)
        if type(jokers) !== bool:
            raise TypeError()
        suits = kwargs.get("suits", (1,2,3,4))
        excl