def personal_assistant():
    Name = input("Hello, I'm Marvin, your personal assistant. What would you like me to refer you as? ").strip().capitalize()
    print(f"Hello, {Name}. That's a nice name.\nPlease {Name}, confirm you're not a robot")
    import sys
    import calendar as cal
    import Verification_module as Ver
    import Arithmetics as Ar
    #The months is a dict that converts the month in string to numbers
    months = {"January" : 1, "Febuary" : 2, "March" : 3, "April" : 4,"May" : 5, "June" : 6, 
              "July" : 7, "August" : 8, "September" : 9, "October" : 10, "November" : 11, "December" : 12}
    #Main function for verification, gender, initiating the Cal function
    def Emma():
        Ver.verification()
        G = input("Can I know your gender?(m/f) ")
        if G == "m":
            print(f"Bro {Name}, I'll be with you throughout this course.", end="\n")
            Cal()
        elif G == "f":
            print(f"Sist {Name}, I'll be with you throughout this course.", end="\n")
            Cal()
        else:
            print("Error: Please try again later.")
            Emma()
        
    #Cal accept input for calendar or arithemetic operation      
    def Cal():
        REQ = input("Would you like to see the calendar?(yes/no) ")
        if REQ == "yes":
            Calen()
        elif REQ == "no":
            Options()
        else:
            print("Error: Invalid input\n")
            Cal()
    #The calendar function displays the calendar
    def Calen():
        yr = (input("Please enter the year in numbers(e.g 2020) "))
        Mt = input("Please enter the month(e.g January) ")
        try:
            yr = int(yr)
            if Mt in months:
                Mt = months[Mt]
                print(cal.month(yr, Mt))
                Options()
            else:
                print("Error: Invalid month. Please enter a valid month.")
                Calen()
        except:
            print("Error: Please enter the year in number")
            Calen()
    #Condition function used by the arithemetic operators
    #takes input wether to continue with operations or exit
    def condition():
        W = input("Would you like to do any other maths?(yes/no) ")
        if W == "yes":
            Options()
        elif W == "no": 
            print(f"Okay nice choice {Name}")
        else:
            print("Error: Invalid input\n")
            condition()
    #The options takes input wether to do any operation
    def Options():
        i = input("Would you like to do any of the following\nAddition(a)\nMultiplication(m)\nSubtraction(s)\nDivision(d)\nOr select (n) for none ")
        if i == "a":
            Ar.sum()
            condition()
        elif i == "m":
            Ar.mul()
            condition()
        elif i == "s":
            Ar.sub()
            condition()
        elif i == "d":
            Ar.div()
            condition()
        elif i == "n":
            print(f"Okay {Name} let's keep maths aside for now")
        else:
            print("Error: I didn't understand your choice. Please try again\n")
            Options()
    Emma()
personal_assistant()