"""
OrderOfNumbers
"""
Number1 = int(input("Enter Number 1: "))
Number2 = int(input("Enter Number 2: "))
Number3 = int(input("Enter Number 3: "))

if Number1 < Number2 and Number2 < Number3:
    print("numbers are ascending")
elif Number1 > Number2 and Number2 > Number3:
    print("numbers are descending")
elif Number1 + Number2 + Number3 > 0:
    if Number1 + Number2 + Number3 % 2 == 0:
        print("no specific order, but all even")
    elif Number1 + Number2 + Number3 % 2 != 0:
        print("no specific order, but all odd")
else: print("no specific order")




"""
SumUp
"""
Number1 = int(input("Enter first number: "))
Number2 = int(input("Enter second number: "))

sum = Number1 + Number2
print(f" The sum of {Number1} and {Number2} is {sum}")

if Number1 <= 0 or Number2 <= 0:
    print("n1 or n2 is < 0")
elif Number1 <= 0 and Number2 <= 0:
    print("n1 and n2 are < 0")
elif Number1 >= 0 and Number2 >= 0 and Number2 < Number1:
    print("Error! N2 needs to be greater than n1")




