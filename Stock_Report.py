
"""
******************************************************************************
* Purpose: Stock Report
*
* @author:  Ramnath Patro
* @version: 1.0
* @since:   26-3-2019
*
******************************************************************************
"""


from oops.oops_utility import object
ref = object


import json

fr = open("Stock_data.json","r")
json_data = json.load(fr)
fr.close()

# print(json_data)

def stock_report():
    print("Each value of Tata share\n")
    tata = ref.stock(json_data["Tata"])
    print(" Total share  of Tata is  :", tata)
    print("\n")

    print("Each value of Relance share\n")
    Relance = ref.stock(json_data["Relance"])
    print("Total share value of Relance :", Relance)
    print("\n")

    print("Each value of Google share\n")
    google = ref.stock(json_data["google"])
    print("Total share value of google :", google)
    print("\n")

    Total_value = tata + Relance + google
    print("All share value is :-", Total_value)
    print()

if __name__ == '__main__':
    while True:
        print("1.Display the Data")
        print("2.Exit")
        inp = input("Enter the option")

        while not inp.isdigit():
            print("Invalid input")
            inp = input()

        inp = int(inp)

        if inp == 1:
            stock_report()

        elif inp == 2:
            print("Exit the program")
            exit()

        else:
            print("Invalid input")




