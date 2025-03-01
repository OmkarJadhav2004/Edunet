#Conditional Statement 
#For Loop 

for i in range(1,11):
    print(f"4 * {i} = {4 * i}")


#table for user input
num = int(input("Enter the Number : "))
for i in range(1,11):
    print(f"{num} * {i} = {num * i}")

#sum of all numbers in a list
nlist = [1,2,3,4,5,6,7,8,9,10]
isum = 0
for i in range(0,len(nlist)):
    isum = isum + nlist[i]
print(isum)
