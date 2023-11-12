def sub():
    try:
        y = int(input("First number? "))
        x = int(input("Second number? "))
        print(f"Result: {y - x}")
    except ValueError:
        print("Error: Try again later")
        sub()
def sum():
    try:
        y = int(input("First number? "))
        x = int(input("Second number? "))
        print(f"Result: {y + x}")
    except ValueError:
        print("Error: Try again later")
        sum()    
def mul():
    try:
        y = int(input("First number? "))
        x = int(input("Second number? "))
        print(f"Result: {y * x}")
    except ValueError:
        print("Error: Try again later")
        mul()
def div():
    try:
        y = int(input("First number? "))
        x = int(input("Second nummber? "))
        print(f"Result: {y // x}")
    except ValueError:
        print("Error: Try again later")
        div()   