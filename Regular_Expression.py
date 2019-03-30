
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

import re

def regex(string):
    constant1 = 0
    while constant1 == 0:
        inp_name = input("Enter the name")
        check_name = re.search(r"^[A-Z][\w][\w]+$", inp_name)
        if check_name:
            print(check_name.group())
            constant1 = 1
        else:
            print("Invalid name ")
    string = re.sub(r"<+[\w]+>+", inp_name, string)

    constant2 = 0
    while constant2 == 0:
        inp_full_name = input("Enter the full name")
        check_full_name = re.search(r"^[A-Z][\w][\w]+\s[A-Z][\w]+$", inp_full_name)
        if check_full_name:
            print(check_full_name.group())
            constant2 = 1
        else:
            print("Invalid full name")
    string = re.sub(r"<+[\w]+\s[\w]+>+", inp_full_name, string)

    constant3 = 0
    while constant3 == 0:
        phone_num = input("Enter the phone Number")
        check_phone_num = re.search(r"^[\d]{10}$", phone_num)
        if check_phone_num:
            print(check_phone_num.group())
            constant3 = 1
        else:
            print("Invalid number")
            print("please enter 10 digit number only")
    string = re.sub(r"[x]{10}", phone_num, string)

    constant4 = 0
    while constant4 == 0:
        date = input("Enter the date")
        check_date = re.search(r"^(0?[1-9]|[12][0-9]|3[01])/(0?[1-9]|1[0-2])/\d\d\d\d$", date)
        if check_date:
            print(check_date.group())
            constant4 = 1
        else:
            print("invalid date"+ " please enter like this:- dd/mm/yyyy")
    string = re.sub(r"\d\d/\d\d/\d\d\d\d", date, string)

    return string




# print(string)



if __name__ == '__main__':
    string = "Hello <<name>>, We have your full name as <<full name>> in our system. your contact number is 91­xxxxxxxxxx. Please,let us know in case of any clarification Thank you BridgeLabz 01/01/2016."
    print(regex(string))








