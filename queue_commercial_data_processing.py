
"""
******************************************************************************
* Purpose: Commercial data processing using queue
*
* @author:  Ramnath Patro
* @version: 1.0
* @since:   29-3-2019
*
******************************************************************************
"""



from Data_Structure_Programs.Datastructure_Operations import queue_anagram
qe = queue_anagram()
import json

from oops.Commercial_data_processing import buy,sell

sell_call = sell
buy_call = buy

class information:
    def customer_company_file_read(file_name, mode):
        fr = open(file_name, mode)
        file_data = json.load(fr)
        fr.close()
        return file_data

    def customer_company_file_write(file_name, customer_details):
        # fw = open(file_name, mode)
        # update_data = json.dump(file_name, fw)
        # fw.close()
        with open(file_name, "w") as file:
            json.dump(customer_details, file)
        return customer_details

    def new_acc(self):
        # customer_details = []
        # company_details = []
        customer_details = information.customer_company_file_read("customer_details.json", "r")
        # company_details = information.customer_company_file_read("company_details.json", "r")

        for element in customer_details:
            qe.enqueue(element)

        while True:
            try:
                inp = int(input("Enter the ID"))
                break
            except:
                print("Invalid ID")
                continue
        while True:
            try:
                for itr in customer_details:
                    # print(itr["customer_id"])
                    if itr["customer_id"] == inp:
                        raise ValueError
                break
            except:
                print("ID present please enter another id")
                inp = input("Enter the another ID")

        inp_name = input("Enter your name")

        while True:
            try:
                inp_bal = int(input("Enter your balance"))
                break
            except:
                print("Invalid balance")
                continue

        new_user = {
            'customer_id': inp,
            'customer_name': inp_name,
            'balance': inp_bal
        }
        # customer_details.append(new_user)
        # customer_details = []
        data = []
        qe.enqueue(new_user)
        for i in range(len(customer_details ) + 1):
            data.append(qe.dequeue())
        customer_details = information.customer_company_file_write("customer_details.json", data)


class search():
    def ser(self):
        customer_details = information.customer_company_file_read("customer_details.json", "r")
        company_details = information.customer_company_file_read("company_details.json", "r")

        while True:
            x = 0
            try:
                inp = int(input("Enter the ID"))
                for itr in customer_details:
                    # print(itr["customer_id"])
                    if itr["customer_id"] == inp:
                        print("Valid ID")
                        x = 1
                        break
                    # if x == 0:
                    #     inp = int(input("Enter the another ID"))
                    # if inp not in itr["customer_id"] and x != 1:
                    #     print("+++++++++++qqqqqqqq")
                    #     raise ValueError
                break
            except:
                print("Invalid ID")
                continue
        print(inp)

        while True:
            try:
                companyname = input("Enter the company Name:").lower()
                if not companyname.isalpha():
                    raise ValueError
                x = 0
                for itr in company_details:
                    for com_name in itr:
                        # print(j)
                        if com_name == companyname:
                            print("Valid ID")
                            x = 1
                            break
                if x == 1:
                    break
            except:
                print("Invalid company name")
                continue
        return inp, companyname
class buy(search):
    def buy_shar(self):
        transaction_name, customer_id, company_name, number_of_share, time_details = buy_call.buy_shar(self)
        try:
            qe = queue_anagram()

            with open('queue_transaction.json', 'r') as myfile:
                details = json.load(myfile)

            for element in details:
                qe.enqueue(element)

            details1 = {"transaction_name ": transaction_name,
                        "customer_id": customer_id,
                        "company_name": company_name,
                        "number_of_share": number_of_share,
                        "time details": time_details
                        }

            qe.enqueue(details1)
            temp = []
            size = qe.size()
            for i in range(size):
                temp.append(qe.dequeue())
            with open('queue_transaction.json', 'w') as data:
                json.dump(temp, data)

        except IOError as e:
            print("File Not Found")
            print(e)
        except Exception as e:
            print(e)

class sell(search):

    def sell_shar(self):
        transaction_name, customer_id, company_name, number_of_share, time_details = sell_call.sell_shar(self)

        try:
            qe = queue_anagram()

            with open('queue_transaction.json', 'r') as myfile:
                details = json.load(myfile)

            for element in details:
                qe.enqueue(element)

            details1 = {"transaction_name ": transaction_name,
                        "customer_id": customer_id,
                        "company_name": company_name,
                        "number_of_share": number_of_share,
                        "time details": time_details
                        }

            qe.enqueue(details1)
            temp = []
            size = qe.size()
            for i in range(size):
                temp.append(qe.dequeue())
            with open('queue_transaction.json', 'w') as data:
                json.dump(temp, data)

        except IOError as e:
            print("File Not Found")
            print(e)
        except Exception as e:
            print(e)


if __name__ == '__main__':

    while True:
        print()
        print("1.create New Account")
        print("2.Buy the share")
        print("3.Sell the share")
        print("4.Exit the program")
        inp = input("Enter the option ")

        while not inp.isdigit():
            print("Invalid input")
            inp = input("Enter the option ")
        inp = int(inp)

        if inp == 1:
            print("create a new Account")
            i = information()
            i.new_acc()

        elif inp == 2:
            print("How much share you buy")
            b = buy()
            b.buy_shar()

        elif inp == 3:
            print("How much share you Sell")
            s = sell()
            s.sell_shar()

        elif inp == 4:
            print("Exit the program")
            exit()

        else:
            print("Invalid Input")





