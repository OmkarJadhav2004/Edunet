#Conditional statements

#-----If statement-----
carbon_footprint = 500.75

if carbon_footprint > 500:
    print("Too high carbon value!")


#even number code
#-----If Else -----
num = int(input("Enter the number to check : "))
print(f"The Number is : {num}")
if num%2 == 0:
    print("Even Number")
else:
    print("Odd Number")

#calculator
#-----If Elif Else-----
num1 = int(input("Enter First Number : "))
num2 = int(input("Enter Second Number : "))
print("------------Menu--------------")
print("For Addition Enter '+' ")
print("For Subtraction Enter '-' ")
print("For Multiplication Enter '*' ")
print("For Division Enter '/' ")
choice = input("Enter your choice : ")[0]

if choice == '+':
    print("Addition is : ",num1+num2)
elif choice == '-':
    print("Subtraction is : ",num1-num2)
elif choice == '*':
    print("Multiplication is : ",num1*num2)
elif choice == '/':
    print("Division is : ",num1/num2)
else:
    print("Enter Correct Choice")

