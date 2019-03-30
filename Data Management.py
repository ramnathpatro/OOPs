

"""
******************************************************************************
* Purpose: Data Management
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

def data_management():
    fr = open("Data Management.json", "r")
    file = json.load(fr)
    fr.close()

    rice = ref.data_management(file["Rice"])
    Pulses = ref.data_management(file["Pulses"])
    Wheat = ref.data_management(file["Wheat"])

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
            data_management()

        elif inp == 2:
            print("Exit the program")
            exit()

        else:
            print("Invalid input")




