# TODO: Write the functions for arithmatic operations here
# These functions should cover Task 2
def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * a


def divide(a, b):
    try:
        return a / b
    except:
        print("float division by zero")


def power(a, b):
    return a ** b


def reminder(a, b):
    return a % b


# -------------------------------------
# TODO: Write the select_op(choice) function here
# This function sould cover Task 1 (Section 2) and Task 3
def select_op(choice):
    return choice


# End the select_op(choice) function here
# -------------------------------------
# This is the main loop. It covers Task 1 (Section 1)
# YOU DO NOT NEED TO CHANGE ANYTHING BELOW THIS LINE

while True:
    print("Select operation.")
    print("1.Add      : + ")
    print("2.Subtract : - ")
    print("3.Multiply : * ")
    print("4.Divide   : / ")
    print("5.Power    : ^ ")
    print("6.Remainder: % ")
    print("7.Terminate: # ")
    print("8.Reset    : $ ")

    # take input from the user
    choice = input("Enter choice(+,-,*,/,^,%,#,$): ")
    print(choice)
    if (select_op(choice) == "#"):
        print("Done. Terminating")
        break
    elif (select_op(choice) == "$"):
        continue



    try:
        a = input("Enter first number: ")
        print(int(a))
    except:
        print(a)
        continue

    try:
        b = input("Enter second number: ")
        print(int(b))
    except:
        print(b)
        continue


    if  (select_op(choice) == "+"):
        print(a, "+", b, "=", add(a, b))
    elif(select_op(choice) == "-"):
        print(a, "-", b, "=", subtract(a, b))
    elif(select_op(choice) == "*"):
        print(a, "*", b, "=", multiply(a, b))
    elif(select_op(choice) == "/"):
        print(a, "/", b, "=", divide(a, b))
    elif(select_op(choice) == "^"):
        print(a, "^", b, "=", power(a, b))
    elif(select_op(choice) == "%"):
        print(a, "%", b, "=", reminder(a, b))
