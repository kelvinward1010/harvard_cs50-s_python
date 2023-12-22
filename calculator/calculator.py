import sys

def plusNumber(x,y,isRound):
    if isRound == "y":
        z = round(x + y)
    elif isRound == "n":
        z = x + y
    print(f"{x} + {y} = {z:.2f}")
    

def multiplyNumber(x,y,isRound):
    if isRound == "y":
        z = round(x * y)
    elif isRound == "n":
        z = x * y
    print(f"{x} * {y} = {z:.2f}")

def divNumber(x,y,isRound):
    if isRound == "y":
        z = round(x / y)
    elif isRound == "n":
        z = x / y
    print(f"{x} / {y} = {z:.2f}")

def subtractNumber(x,y,isRound):
    if isRound == "y":
        z = round(x - y)
    elif isRound == "n":
        z = x - y
    print(f"{x} - {y} = {z:.2f}")
    

def calculator():
    
    select_calculation = input("\nSelect the calculation you want to calculate: \n1. Plus\n2.Multiply\n3.Divide\n4.Subtract\nType your calculation: ")
    if select_calculation not in ["1", "2", "3", "4"]:
        print(f"\nPlease select 1 or 2 or 3 or 4!".center(30,'='))
        return calculator()
    
    x = float(input("What's x? "))
    y = float(input("What's y? "))
    isRounding = input("Do you want to round numbers? [y/n]: ")
    
    if select_calculation == "1":
        return plusNumber(x,y, isRound=isRounding)
    elif select_calculation == "2":
        return multiplyNumber(x,y,isRound=isRounding)
    elif select_calculation == "3":
        return divNumber(x,y, isRound=isRounding)
    else:
        return subtractNumber(x,y, isRound=isRounding)
    
calculator()
    
    