
"""
******************************************************************************
* Purpose: Commercial data processing
*
* @author:  Ramnath Patro
* @version: 1.0
* @since:   28-3-2019
*
******************************************************************************
"""



import json
import datetime

# fr = open("company_details.json","r")
# company_details = json.load(fr)
# fr.close()
# print(company_details)
#
# for company_name in company_details:
#     for data in company_name:
#         print(data,company_name[data]) #["number_of_share"]
#     # print(i)
#
# print("***************")

"""information class is using for file read, write and new Account """
class information:
    """read the json file"""
    def customer_company_file_read(file_name, mode):
        fr = open(file_name, mode)
        file_data = json.load(fr)
        fr.close()
        return file_data

    """Write the json file"""
    def customer_company_file_write(file_name,customer_details):
        # fw = open(file_name, mode)
        # update_data = json.dump(file_name, fw)
        # fw.close()
        with open(file_name,"w") as file:
            json.dump(customer_details, file)
        return customer_details

    """create the new Account"""
    def new_acc(self):
        customer_details = []
        # company_details = []
        customer_details = information.customer_company_file_read("customer_details.json", "r")
        # company_details = information.customer_company_file_read("company_details.json", "r")

        """use for id validation"""
        while True:
            try:
                inp = int(input("Enter the ID"))
                break
            except:
                print("Invalid ID")
                continue

        """use for id validation(in the list id is present or not)"""
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
        """use for balance is digit or not"""
        while True:
            try:
                inp_bal = int(input("Enter your balance"))
                break
            except:
                print("Invalid balance")
                continue

        """create new user"""
        new_user = {
            'customer_id': inp,
            'customer_name': inp_name,
            'balance': inp_bal
        }
        customer_details.append(new_user)
        print(customer_details)
        customer_details = information.customer_company_file_write("customer_details.json",customer_details)

""" search class is use searching the id and company """
class search():
    def ser(self):
        customer_details = information.customer_company_file_read("customer_details.json", "r")
        company_details = information.customer_company_file_read("company_details.json", "r")
        # self.inp = inp
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
                if x == 1:
                    break
                else:
                    raise ValueError
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

        return inp,companyname


class buy(search):
    def buy_shar(self):
        customer_details = information.customer_company_file_read("customer_details.json", "r")
        company_details = information.customer_company_file_read("company_details.json", "r")
        id, bank_name = self.ser() # inheritance the property
        # print(x)
        # print(y)
        buy_shr_inp = int(input("How much share you BUY")) # user input
        
        if company_details[0][bank_name]['number_of_share'] < buy_shr_inp: # check the input shar is not grater the company share
            print("company have less shares")
        else:
            print(company_details[0][bank_name]['number_of_share'])

            conu = 0
            for customer in customer_details:
                conu += 1
                for data in customer:
                    if customer[data] == id and data == 'customer_id':
                        # print(conu)
                        ind = conu
                        break

            customer_data = customer_details.pop(ind - 1)
            # print(customer_details)
            print("cust_data",customer_data)
            # customer_data[bank_name] =
            try:
                if customer_data[bank_name]:
                    print("+++++", customer_data[data])

                    customer_data[bank_name] = customer_data[bank_name] + buy_shr_inp
                    print(customer_data[bank_name])

                    pur = (company_details[0][bank_name]['number_of_share']) - buy_shr_inp
                    company_details[0][bank_name]['number_of_share'] = pur
                    print(company_details)

                    cost = company_details[0][bank_name]['per_share_cost'] * buy_shr_inp
                    co_bal = (company_details[0][bank_name]['balance']) + cost
                    company_details[0][bank_name]['balance'] = co_bal

                    bal = customer_data['balance'] - cost
                    customer_data['balance'] = bal

                    print(customer_data)
                    #
                    customer_details.insert(ind - 1, customer_data)
                    #
                    print(customer_details)
            except:
                customer_data[bank_name] = buy_shr_inp

                pur = (company_details[0][bank_name]['number_of_share']) - buy_shr_inp
                company_details[0][bank_name]['number_of_share'] = pur
                # print(company_details)

                cost = company_details[0][bank_name]['per_share_cost'] * buy_shr_inp
                co_bal = (company_details[0][bank_name]['balance']) + cost
                company_details[0][bank_name]['balance'] = co_bal

                bal = customer_data['balance'] - cost
                customer_data['balance'] = bal

                print(customer_data)

                customer_details.insert(ind - 1, customer_data)




            print(customer_details)
            print(company_details)
            customer_details = information.customer_company_file_write("customer_details.json", customer_details)
            company_details = information.customer_company_file_write("company_details.json", company_details)

        return "Buy", id, bank_name, buy_shr_inp, str(datetime.datetime.now())


class sell(search):

    def sell_shar(self):
        customer_details = information.customer_company_file_read("customer_details.json", "r")
        company_details = information.customer_company_file_read("company_details.json", "r")
        id, bank_name = self.ser()

        sell_shr_inp = int(input("How much share you SELL"))


        # print(customer_details)
        conu = 0
        for customer in customer_details:
            conu += 1
            for data in customer:
                if customer[data] == id and data == 'customer_id':
                    ind = conu
                    break

        customer_data = customer_details.pop(ind - 1)
        print(customer_data)





        try:
            if customer_data[bank_name]:
                if customer_data[bank_name] > sell_shr_inp:
                    customer_data[bank_name] = customer_data[bank_name] - sell_shr_inp
                    pur = (company_details[0][bank_name]['number_of_share']) + sell_shr_inp
                    print("xxxxxxxxxx", pur)
                    company_details[0][bank_name]['number_of_share'] = pur
                    print(company_details)

                    cost = company_details[0][bank_name]['per_share_cost'] * sell_shr_inp
                    co_bal = (company_details[0][bank_name]['balance']) - cost
                    company_details[0][bank_name]['balance'] = co_bal
                    # print(company_details)

                    bal = customer_data['balance'] + cost
                    customer_data['balance'] = bal

                    customer_details.insert(ind - 1, customer_data)
                    # print(customer_data[bank_name])
                    # print(customer_data)
                    # print(customer_details)
                    # print(company_details)
                    customer_details = information.customer_company_file_write("customer_details.json",
                                                                               customer_details)
                    company_details = information.customer_company_file_write("company_details.json", company_details)
                else:
                    print("you have less share")
                    customer_details.insert(ind - 1, customer_data)
                    # print(customer_details)
                    # print(company_details)
                    customer_details = information.customer_company_file_write("customer_details.json",
                                                                               customer_details)
                    company_details = information.customer_company_file_write("company_details.json", company_details)

        except:
            print("you do not have", bank_name," company shar ")

        return "Sell", id, bank_name, sell_shr_inp, str(datetime.datetime.now())



if __name__ == '__main__':

    while True:
        print("1.create New Account")
        print("2.Buy the share")
        print("3.Sell the share")
        print("4.Exit the program")
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
            # print(x)

        elif inp == 3:
            print("How much share you Sell")
            s = sell()
            x = s.sell_shar()
            print(x)

        elif inp == 4:
            print("Exit the program")
            exit()

        else:
            print("Invalid Input")





