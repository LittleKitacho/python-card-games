# About cardfuntions.py

`cardfunctions.py` is used (internally) for functions that would otherwise be
written over and over and over (etc.) again.  Details on the functions will
be detailed, as well as the ID system for cards.  Read up on this if you
wish to create your own cards.

## The ID system for cards

The idea for the ID system is that each card in a regular card deck has a
specific ID.  Humans can understand this system, you can find a chart of
all the IDs [here](./ids-cardfunctions.md) if you do not wish to do math.

To understand it, first understand that jokers are IDs 0 and 1.
Subtracting 1 from the ID of non-jokers gives a 1-indexed number that
represent a card.  If the ID is less than 14, then the card is a Spade, and the
ID is the number of the card (1 = Ace, 11/12/13 = Jack/Queen/King
respectively).  If it is more than 13, though, subtract 13 from the ID, and the
card is a Club if the ID is now under 14, with the number being the ID of the
card.  If the ID is still over 13, subtract 13 again and the card is a Heart,
with the ID being the number unless the ID is still over 13.  Then subtract 13
yet again and the card is a diamond, with the number being the ID.  If the ID
is over 13 now, that ID is an illegal ID, and cannot be used.
