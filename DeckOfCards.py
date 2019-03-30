from oops.oops_utility import Deck_Of_Cards

if __name__ == '__main__':

    while True:
        print("1.play")
        print("2.Exit")
        inp = input("Enter the option")
        while not inp.isdigit():
            print("Invalid input")
            inp = input("Enter the option ")

        inp = int(inp)

        if inp == 1:
            d = Deck_Of_Cards()
            d.deck()
            d.cards_to_players()
            d.display()

        elif inp == 2:
            print("Exit the program")
            exit()

        else:
            print("Invalid input")





