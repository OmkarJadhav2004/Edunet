#Electricity Bill Calculator

def billCalc(unit):
    bill = 0
    if unit < 100:
        bill = unit * 5
        return bill
    elif unit >= 100 and unit <= 200:
        bill = unit * 7
        return bill
    elif unit > 200:
        bill =unit * 10
        return bill
    else:
        print("Enter Valid Unit")
        return 


eUnit = int(input("Enter the Number of Units : "))
print("Number of Units are : ",eUnit)

x = billCalc(eUnit)
print(f"Your Electricity Bill is : {x}")
