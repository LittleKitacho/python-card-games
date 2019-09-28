import random
from os import name, system
from time import sleep

print('You can sudgest names for me!  Please read up on \'naming.md\' for more information!')

def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')

deck = [1,2,3,4,5,6,7,8,9,10,11,12,13,1,2,3,4,5,6,7,8,9,10,11,12,13,1,2,3,4,5,6,7,8,9,10,11,12,13,1,2,3,4,5,6,7,8,9,10,11,12,13]
freeCards = []
while freeCards.len <= 4:
    take = random.randint(1, deck.len + 1)
    freeCards.append(deck[take])
    deck.remove(deck[take])
players = int(input("How many players are playing? (only input a number)"))
pDecks = [], turn = 0
while pDecks.len <= players:
    pDeck = []
    pDeck.append(input('What is player '+ (pDecks.len + 1) +"'s name?"))
    while pDeck.len <= 7:
        take = random.randint(0, deck.len)
        pDeck.append(deck[take])
        deck.remove(deck[take])
    print('Ok, '+ pDeck[1] +'!')
    pDecks.append(pDeck)
print('The decks have been assigned, time to play!')
turn = 1
sleep(3)
clear()

def checkWin():
    s1 = 1
    s2 = 2
    s3 = 3
    s4 = 4
    while true:
        if s1 != s2 && s1 != s3 && s1 != s4 && s2 != s3 && s2 != s4 && s3 != s4
            card1 = pDecks[turn[s1]]
            card2 = pDecks[turn[s2]]
            card3 = pDecks[turn[s3]]
            card4 = pDecks[turn[s4]]
            if card1 == card2 && card1 == card3 && card1 == card4 && card2 == card3 && card2 == card4 && card3 == card4:
                return True
            else:
                return False
        s1 ++
        s2 ++
        s3 ++
        s4 ++

            
                

while !checkWin():
    input('Press enter when only '+ pDecks[turn[1]] +' is looking at the screen.')
    print('Here is your deck:\n'+ pDecks[turn] +'\nAnd here are the free cards:\n'+ freeCards +'\n\n')
    print('What do you wish to do?')
    while !checkWin:
        input = int(input('[1 = Take Free Card 1]\n[2 = Take Free Card 2]\n[3 = Take Free Card 3]\n[4 = Take Free Card 4]\n[5 = Draw from stack]'))
        if input === 1||2||3||4:
            freeCard = input
            input = int(input('Which card would you like to place back?\n[Type the place of your card.]'))
            pDecks[turn.append(freeCards[freeCard])]
            freeCards.remove(freeCard)
            freeCards.insert(freecard, pDecks[turn[do]])
        elif input === 5:
            take = random.randint(0, deck.len)

print('Winner Winner (Chicken Dinner!)')
print(pDecks[turn[1]] +' Wins!')
print('\nThis game is over.  Please restart the script to play again.')