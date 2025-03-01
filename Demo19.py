#function

def greet(name):
    print("Hello : ",name)

greet("omkar")

def add(a,b):
    c = a+b
    return c

x = add(10,20)
print(x)

print("-------------------------")

#function takes 3 parameters and return max
def maxi(num1,num2,num3):
    if num1 > num2 and num1 > num3:
        return num1
    elif num2 > num1 and num2 > num3:
        return num2
    else:
        return num3

x = maxi(69,12,6)
print("Maximum is : ",x)