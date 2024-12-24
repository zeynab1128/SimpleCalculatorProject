def add(x, y) :
    return(x + y)

def subtract(x, y) :
    return(x - y)

def multiply(x, y) :
    return(x * y)

def divide(x, y) :
    return(x / y)

def is_number(num) :
    try:
        float(num)
        return True
    except TypeError:
        return False

while True:
    print("Please enter the Operations number you wish to use:\n1)Addition (+)\n2)Subtraction (-)\n3)Multiplication (*)\n4)Division (/)\n5)Exit")
    num_operation = input()
    if num_operation == "5":
        break

    print("Enter first number:")
    x = float(input())
    if is_number(x):
        pass
    else:
        print("TypeError called")

    print("Enter second number:")
    y = float(input())
    if y == 0 :
        raise ZeroDivisionError("Do not divide by zero!")
    elif is_number(y):
        pass
    else:
        print("TypeError called")

    if num_operation == "1":
        print(f"the result is: {add(x, y)}")
    elif num_operation == "2":
        print(f"the result is: {subtract(x, y)}")
    elif num_operation == "3":
        print(f"the result is: {multiply(x, y)}")
    elif num_operation == "4":
        print(f"the result is: {divide(x, y)}")

    print("*_**_**_**_**_**_**_**_**_**_*")