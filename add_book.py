"""
Overview : To maintain an address book.
purpose : Show the menu list to user
class name : AddressBook
author :
date :
"""

from oops.add_ser import Service


class AddressBook:
    def __init__(self):

        self.obj = Service()

    def address_book(self):
        """
        :return:
        """
        try:
            while True:
                print("**************************************************")
                print("1.Create\n2.Open\n3.Save\n4.Save As\n5.Add Person\n6.Delete Person\n7.Edit Person\n8.Quit")

                choice_selected = int(input("Select any choice : "))
                if choice_selected == 8:
                    self.obj.save()
                    print("Exited")
                    return
                elif choice_selected > 8:
                    print("You have selected wrong choice.")
                    continue
                choice = {1: "create", 2: "open", 3: "save", 4: "save_as",
                          5: "add_person", 6: "delete_person", 7: "edit_person"}
                fun = getattr(self.obj, choice[choice_selected])
                fun()
        except Exception as e:
            print("You have enter wrong input.")
            self.address_book()




# Main method
if __name__ == "__main__":
    """
    """
    obj = AddressBook()
    obj.address_book()