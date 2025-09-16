number = input("Give me a number: ")
try:
    if float(number) == int(float(number)):
        print("This number is an integer.")
    else:
        print("This number is a decimal.")
except ValueError:
    print("This number is not a valid number.")