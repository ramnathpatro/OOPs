
"""
******************************************************************************
* Purpose: oops Utility class
*
* @author:  Ramnath Patro
* @version: 1.0
* @since:   26-3-2019
*
******************************************************************************
"""


import random

class object:

    def data_management(x):
        for i in x:
            print(i["name"], ":- weight is :", i["weight"], "price is:", i["price"], " Total amount:-",
                  i["weight"] * i["price"], "\n")

    def stock(json_data):
        value_Tata = 0
        for data in json_data:
            print(data["name"], ":- No of Share is,", data["no_of_share"], "price of each share", data["price"],
                  ",value of share is", data["no_of_share"] * data["price"])
            value_Tata = value_Tata + data["no_of_share"] * data["price"]
        return value_Tata

    # def new_acc(customer_details):
    #     # fr = open("customer_details.json", "r")
    #     # customer_details = json.load(fr)
    #     # fr.close()
    #     # print(customer_details)
    #
    #     con = 0
    #     while con == 0:
    #         inp = input("Enter the ID")
    #         check_num = re.search(r"^[\d]+$", inp)
    #         if check_num:
    #             inp = int(inp)
    #             con = 1
    #             for itr in customer_details:
    #                 # print(itr["customer_id"])
    #                 if itr["customer_id"] != inp:
    #                     continue
    #                 else:
    #                     print("ID is present please enter another id ")
    #
    #     inp_name = input("Enter the name")
    #     while not inp_name.isalpha():
    #         print("Invalid first name only")
    #         inp_name = input()
    #
    #     bal = input("Enter the Balance")
    #     while not bal.isdigit():
    #         print("Invalid bal,enter number only")
    #         bal = input()
    #     value = {"customer_id": inp, "customer_name": inp_name, "balance": bal}
    #     customer_details.append(value)
    #
    #     # fw = open("customer_details.json", "w")
    #     # json.dump(customer_details, fw)
    #     # fw.close()

class Deck_Of_Cards:
    def __init__(self):
        """
        it is the constructor of the Deck_Of_Cards Class
        card:it is having dictionary of cards
        suit:it is list of suit cards
        rank:it is the list of rank
        player1,player2,player3,player4:all are dictionaries
        player:it is the tuple for each player

        """
        self.card = {'Clubs': [], 'Diamonds': [], 'Hearts': [], 'Spades': []}
        self.suit = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
        self.rank = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
        self.Player1 = {'Clubs': [], 'Diamonds': [], 'Hearts': [], 'Spades': []}
        self.Player2 = {'Clubs': [], 'Diamonds': [], 'Hearts': [], 'Spades': []}
        self.Player3 = {'Clubs': [], 'Diamonds': [], 'Hearts': [], 'Spades': []}
        self.Player4 = {'Clubs': [], 'Diamonds': [], 'Hearts': [], 'Spades': []}
        self.player = (self.Player1, self.Player2, self.Player3, self.Player4)

    def deck(self):
        """
        deck method will append the items to the card dictionary which are generated randomly
        return it will not return anything
        """
        count = 36
        while count > 0:
            random_suit = self.suit[random.randrange(0, 4, 1)]
            random_rank = self.rank[random.randrange(0, 13, 1)]
            temp = self.card[random_suit]
            flag = True
            for i in range(len(temp)):
                if temp[i] == random_rank:
                    flag = False
                    break
            if flag:
                self.card[random_suit].append(random_rank)
                count -= 1

    def cards_to_players(self):
        """ this method will distribute the cards to the players return will not return anything """
        count = 0
        for i in self.suit:
            temp = self.card[i]
            for j in range(len(temp)):
                if count >= 4:
                    count = 0
                self.player[count][i].append(temp[j])
                count += 1

    def display(self):
        """
        this method will display the cards of each players
        return it will not return anything
        """
        print()
        print("Display Cards:")
        print()
        for i in range(len(self.player)):
            print()
            print('===player====', i + 1)
            print()
            print('Clubs: ', self.player[i]['Clubs'])
            print('Diamonds: ', self.player[i]['Diamonds'])
            print('Hearts:', self.player[i]['Hearts'])
            print('Spades:', self.player[i]['Spades'])

