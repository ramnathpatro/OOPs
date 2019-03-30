
"""
******************************************************************************
* Purpose: distrute 9 card to 4 player and print the card the recieved by the
*          4 player
* @author:  Ramnath Patro
* @version: 1.0
* @since:   30-3-2019
*
******************************************************************************
"""

import random
import itertools

class DeckOfCard:

    def card_operation(self):

        deck = list(itertools.product([2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A'],
                                      ['Spade', 'Heart', 'Diamond', 'Club']))
        random.shuffle(deck)
        print(len(deck))
        # draw cards, a total of 36 cards divided among 4 players each player get 9 card
        print("Player 1 got:")
        for pl1 in range(9):
            print(deck[pl1], end=" ")
            deck.remove(deck[pl1])

        print()
        print("Player 2 got:")
        for pl2 in range(9):
            print(deck[pl2], end=" ")
            deck.remove(deck[pl2])

        print()
        print("Player 3 got:")
        for pl3 in range(9):
            print(deck[pl3], end=" ")
            deck.remove(deck[pl3])

        print()
        print("Player 4 got:")
        for pl4 in range(9):
            print(deck[pl4], end=" ")
            deck.remove(deck[pl4])


""" main function """
if __name__ == '__main__':

    while True:
        print()
        print("1.Play")
        print("2.Exit")

        inp = input("Enter the option")

        while not inp.isdigit():
            print("Invalid input")
            inp = input()

        inp = int(inp)

        if inp == 1:
            myClass = DeckOfCard()
            myClass.card_operation()

        elif inp == 2:
            print("Exit the program")
            exit()

        else:
            print("Invalid input")


