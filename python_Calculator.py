# calculator making
num = int(input(" Enter Number : "))
opt = input("enter operator to Do calculations ex - [ + , - , * , / ]")
senum = int(input(" Enter a second no "))
if opt == "+":
    print(f"the addition of num is {num + senum}")
elif opt == "-":
    print(f" the subtraction of your number {num - senum}")
elif opt == "*":
    print(f" the maultiplication is you number { num * senum}")
    

elif opt == "/":
    print(f" division of  your no {num / senum}")
else:
    print("Invalid operations ! ")
    
print("-------------------------- second calculators------------")
    
# calutors with another methods
def add(a, b):
    print(f"the sum of your number {a + b}")
def sub(a, b):
    print(f"the sum of your number {a - b}")
def multiple(a, b):
    print(f"the sum of your number {a * b}")
def divide(a, b):
    print(f"the sum of your number {a / b}")
    
def null():
        print(f"invalid operation of {a } and {b}")
        
a1 = int(input("Enter the Number :  "))
print("A for Additions")
print("B for Additions")
print("C for Additions")
print("D for Additions")
choise = input("input your choise :  ")
b2 = int(input("Enter a Second Number : "))
if choise == "a" or choise=="A":
    add(a1 , b2)
elif choise == "b" or choise == "B":
    sub(a1, b2)
elif choise == "c" or choise == "C":
    multiple(a1, b2)
elif choise == "d" or choise == "D":
    sub(a1, b2)
else :
    divide()





