listofgoods = []
prices = []


#Makinglist takes data from the user
def Makinglist():
    try:
        while True:
            name = input("Please input an item and type 'done' when you done ")
            if name.strip().lower() == 'done':
                 opt()
                 break
            elif name == '':
                print("You entered didn't input an item name\n")
            elif name == ' ':
                print("You entered didn't input an item name\n")
            elif name == '   ':
                print("You entered didn't input an item name\n")
            elif name.strip().upper() in listofgoods:
                print("\nThis item is already in the list\n")
            #elif not isinstance(name, str):
            #        print("You didn't input an item name..\n")
            else:
                listofgoods.append(name.strip().upper())
            print(listofgoods)
            
    except ValueError:
        print("Please try again later")


#Ask for correction or verified
def opt():
    m = input(f"Is this correct? {listofgoods}(yes/no) ")
    if m.strip().lower() == "yes":
        pricesfunc()
    elif m.strip().lower() == "no":
        oppourtunity()
    else:
        print("Your answer not found!")
        opt()


#this function helps with the correction of the items
def oppourtunity():
    user = input("Please press 'r' to redo\n'c'to correct a particular item\n'p' to remove an item\n")
    if user.strip().lower() == "r":
        print("We'll redo it then!.. please be careful this time\n")
        listofgoods.clear()
        prices.clear()
        Makinglist()
    elif user.strip().lower() == "c":
        for i in range(0, len(listofgoods)):
            print({i}, {listofgoods[i]})
        c = int(input("Please input the index number of the particular item, ranging from 0 to ...\n"))
        if c in range(0, len(listofgoods)):
            n = input(f"Please type in the correct item in replace for {listofgoods[c]} ")
            listofgoods[c] = n.strip().upper()
            print("Your new list: ")
            for m in range(0, len(listofgoods)):
                print(listofgoods[m])
            opt()
        else:
            print("Your choice was not found.")
            oppourtunity()
    elif user.strip().lower() == "p":
        for i in range(0, len(listofgoods)):
            print({i}, {listofgoods[i]})
        c = input("Please input the index number of the particular item you want to remove\n")
        try:
            c = int(c)
            if c in range(0, len(listofgoods)):
                listofgoods.pop(c)
            print("Your new list: ")
            for m in range(0, len(listofgoods)):
                print(listofgoods[m])
            opt()   
        except:
            print("An error occured\n")
            oppourtunity() 
    else:
        print("Your choice not found.\n\n")
        oppourtunity()


#pricesfunc takes input of the prices
def pricesfunc():
        #while True:
                try:
                    print("Please input the prices of the items accordingly\nType 'FREE' for any free item\nType 'done' when you done\n")
                    for i in listofgoods:
                        name = input(f"{i} : ")
                        if name == '':
                            print("You didn't input a price\n")
                        elif name == ' ':
                            print("You didn't input a price\n")
                        elif name == '   ':
                            print("You didn't input a price\n")
                    #elif isinstance(name, str):
                    #    print("You didn't input a price..\n")
                        elif len(listofgoods) == len(prices):
                            func()
                        elif name.lower() == 'done':
                            if len(listofgoods) == len(prices):
                                func()
                            else:
                                print("The prices inputted does not match the list of items available, please provide the complete prices\n")
                        else:
                            prices.append(name)
                                        
                    #if name == str(name):
                    #    print("You didn't input a number")
                    #    continue
                    mydict = dict(zip(listofgoods, prices))
                    print(mydict)
                    choice()
                    #break       
                except ValueError:
                    print("Prices of goods not inputted in numbers, please try again later")
                    pricesfunc()


#this function corrects the prices
def opp():
    user = input("Please press 'r' to redo\n'c'to correct a particular item\n")
    if user.strip().lower() == "r":
        print("We'll redo it then!.. please be careful this time")
        prices.clear()
        pricesfunc()
    elif user.strip().lower() == "c":
        for i in range(0, len(listofgoods)):
            print({i}, {listofgoods[i]}, {prices[i]})
        c = int(input("Please input the index number of the particular price, ranging from 0 to ...\n"))
        if c in range(0, len(prices)):
            n = input(f"Please type in the correct price in replace of {prices[c]} ")
            prices[c] = n
            func()
        else:
            print("Your choice was not found.")
            opp()
    else:
        print("Your choice not found\n")
        opp()


#prints out the list of goods and direct to choice
def func():
    print("Your new list:")
    sdict = dict(zip(listofgoods, prices))
    print(sdict)
    choice()


#Choice asks and ease correction. Directs the backend to frontend with START
#The start of START, welcome's customer, list out all available product
def choice():
    mydict = dict(zip(listofgoods, prices))
    m = input(f"Is that correct?(yes/no) ")
    if m.strip().lower() == "yes":
        print("Nice!")
        def start():
            act = input("Can't wait to serve customers\n\nPlease type 'START' to activate...\n")
            if act.strip().upper() == 'START':
                print("\n\nHello, welcome to Emma's place. What would you like from the list below? \n")
                calc()
            else:
                print("An error occured\n\n")
                start()
        start()
    elif m.strip().lower() == "no":
        print("Okay\n")
        ni = input("Please input 'i' to correct one of the item name or 'p' to correct the price of an item\n")   
        if ni.strip().lower() == "i":
            oppourtunity()
        elif ni.strip().lower() == "p":
            opp()
        else:
            print("An error occured.\n")
            choice()
    else:
        print("Your answer not found!")
        choice()


#Ask for customer's choice, calculate
list1 = []
list2 = []
last_fruit_price = []
def calc():
    freeitems = []
    freeitemsp = []
    answer = 0
    for i in range(len(listofgoods)):
        print(listofgoods[i], ":$", prices[i])
    mydict = dict(zip(listofgoods, prices))
    m = input("\nPlease what you want from the above? ")
    if m.strip().upper() in mydict:
        while True:
            try:
                n = int(input(f"How many {m} do you want? "))
                s = mydict.get(m.upper())
                if s == "FREE":
                    print(f"{m} is FREE!")
                    freeitems.append(m)
                    freeitemsp.append(n)
                else:
                    print(f"The price of 1 {m} is ${s}")
                    s = int(s)
                    mee = s * n
                    list2.append(m)
                    print(f"{n} {m}(s) is worth {mee}")
                    list1.append(mee)
                    last_fruit_price.append(n)

                if list1 != 0:
                    answer = sum(list1)
                    for i in range(len(list2)):
                        print(f"\nITEM: {list2[i]}, AMOUNT: {last_fruit_price[i]}, PRICE: {list1[i]}\n")
                    print("Total: ", answer)
                else:
                    continue
                if freeitems:
                    print(f"You got {freeitemsp} of FREE {freeitems}\n\n")
                h = input("Would you like any more thing from the list?(yes/no) ")
                if h.strip().lower() == "yes":
                    calc()
                    break
                elif h.strip().lower() == "no":
                    for i in range(len(list2)):
                        print(f"\n ITEM: {list2[i]}, AMOUNT: {last_fruit_price[i]}, PRICE: {list1[i]}\n")
                    print("Your total goods, is worth: $", answer)
                    print("\nThank you for your patronage.\n")
                    break
                else:
                    print("Your answer is not recognised.\n")
                    calc()
                    break 
            except: 
                print("please try again")
                calc()
                break
    else:
        num = input(f"Your choice was not found or we probably don't have {m}\nPlease input 't' to try again or 'q' to quit\n")
        if num.lower() == "t":
            for i in range(len(listofgoods)):
                print(listofgoods[i], ":$", prices[i])
            calc()
        elif num.strip().lower() == "q":
            mw = input("Are you sure you want to quit?(y/n) ")
            if mw.strip().lower() == "y":
                return
            elif mw.strip().lower() == "n":
                calc()
            else:
                pass
        else:
            print("Please your choice is not recognised.\nThank you for your patronage.")


if __name__ == '__main__':
    Makinglist()