s = result = []
print("This is a to-do list.")
def todo():
    Reply = input("Press A to add a task, D to delete a task and C mark a task completed ")
    if Reply == "A":
        Add()
    elif Reply == "D":
        delete()
    elif Reply == "C":
        complete()
    else:
        print("Your choice wasn't found. Please try again later")


def Add():
    import Verification_module as ver
    ver.verification()
    try:
        n = int(input("How many tasks do you want to add today? "))
        for n in range(n):
            w = (input(f"Task{n}: "))
            result.append(w)
        ans = input("Please input 'C' to mark a task completed, 'D' to delete a task or 'N' to do nothing ")
        if ans == "C":
            complete()
        elif ans == "D":
            delete()
        elif ans == "N":
            return
        else:
            print("Choice not found, please try again later.")
    except ValueError:
            print("You didn't input the number of tasks you want to add correctly. Pleasee try again later.")
        

def delete():
    import Verification_module as ver
    ver.verification()
    try:
        nn = input("Would you like to see your already existing tasks?(yes/no) ")
        if nn == "yes":
            print("Your tasks available: ")
            for I in s:                    
                print(I)
        elif nn == "no":
            print("Okay, nice choice")
        h = int(input("To delete, write the task number. E.g, 0 to delete task 0\n"))
        if h in range(0, 999):
            result.pop(h)
            print(f"Task{h} succesfully deleted.")
            print("Your new list is: ")
            for d in result:
                print(d)
            inp = input("Do you want to delete any other task?(yes/no) ")
            if inp == "yes":
                delete()
            elif inp == "no":
                print("OK!")
            else:
                print("Choice not found, please try again later.")
        else:
                print("Out of bound")
    except ValueError:
            print("You didn't input the number of the task you want to delete correctly. Please try again later.")


def complete():
    C = "No"
    data = {"Tasks" : result, "Completed" : C}
    import pandas as pd
    res = pd.DataFrame(data)
    if len(res) == 0:
        print("There's no data to show. Please add a task first")
        Add()
        complete()
    else:
        nn = input("Would you like to see your already existing tasks?(yes/no) ")
        if nn == "yes":
            print(res)
        elif nn == "no":
            print("Okay, nice choice")
        else:
            print("Choice not found, please try again later.")
        try:
            r = int(input("Which task do you want to mark as complete? Input in number. "))
            res.loc[r, "Completed"] = "yes"
            print("New list of to-do tasks: ")
            print(res)
        except ValueError:
            print("Please try again later.")

todo()
