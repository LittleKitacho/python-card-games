class Card():
    '''Basic class for a card.

    Contains variables used for rendering cards and dealing with card game logic.
    '''
    def __init__(self, id: int, **kwargs):
        '''Creates card using an ID.

        See about-cardfunctions.md for information about creating cards.

        Creating a deck automatically creates cards, so you shouldn't have to create more
        (unless you are using them as a display).
        '''
        startFlipped = kwargs.get("flipped", False)

        self.id = id
        # Data assignment from ID.
        if id == 0 or id == 1:
            if id == 0:
                self.suit = 0
                self.colored = False
                self.number = 0
            elif id == 1:
                self.suit = 0
                self.colored = True
                self.number = 0
        elif 2 <= id <= 

        self.flipped = startFlipped

    def flip(self):
        '''Flips a card.

        Can also be done by toggling the 'card.flipped', but is not recommended.

        Doesn't work if called from the class instead of an object.
        '''

class Deck():
    def __init__(self, **kwargs):
        self.cards = []
        includes_jokers = kwargs.get("jokers", False)
        if type(jokers) == bool:
            raise TypeError()
        suits = kwargs.get("suits", (1,2,3,4))
        exclude = kwargs.get("exclude", [])
        include = kwargs.get("include", [])

        if includes_jokers:
            self.cards.append(Card(0), Card(1))
            for i in suits:
                for n in range(2 + ((i - 1) * 13), 2 + (i * 13))
