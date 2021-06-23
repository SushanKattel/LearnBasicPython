try:
    y = 4/0
    number = int(input("Enter a number: "))
    print(number)
except ValueError:
    print("INVALID INPUT.")
except ZeroDivisionError:
    print("Divided by zero!!")



