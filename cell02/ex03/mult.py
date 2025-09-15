number1 = int(input("Inpur Num1: "))
number2 = int(input("Input Num2: "))
mult = number1*number2
print(f"{number1} x {number2} = {mult}")
if(mult>0):
    print("The result is positive.")
elif(mult<0):
    print("The result is negative.")
elif(mult==0):
    print("The result is positive and negative.")