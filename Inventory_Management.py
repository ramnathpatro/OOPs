
"""
******************************************************************************
* Purpose: Regular Expression
*
* @author:  Ramnath Patro
* @version: 1.0
* @since:   26-3-2019
*
******************************************************************************
"""

from oops.oops_utility import object
ref = object
import re
import json

fr = open("Data Management.json", "r")
file = json.load(fr)
fr.close()


while True:
    print("1.Rice")
    print("2.Puses")
    print("3.Wheat")
    print("4.Exit")

    inp = input("Which product price you wand ")

    check = re.search(r"^[\d]$", inp)

    if check:
        inp = int(inp)
        if inp == 1:
            rice = ref.data_management(file["Rice"])

        elif inp == 2:
            Pulses = ref.data_management(file["Pulses"])

        elif inp == 3:
            Wheat = ref.data_management(file["Wheat"])

        elif inp == 4:
            print("Exit")
            exit()

        else:
            print("Invalid Input")

    else:
        print("Invalid Input")

