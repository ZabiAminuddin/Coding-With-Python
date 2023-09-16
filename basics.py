
def evenOrOdd(num):
    if(num % 2 == 0):
        print("Its an even number")
    else:
        print("Its an Odd number")

def greatNum(num1, num2):
    if(num1 > num2):
        print("Num1 is greater")
    else:
        print("Num2 is greater")

num = int(input("Enter a number: "))

evenOrOdd(num)

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

greatNum(num1, num2)