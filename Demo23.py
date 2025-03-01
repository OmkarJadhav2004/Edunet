#Vehicle Insurance Premium

vPrice = float(input("Enter the Price of Vehicle : "))
Vage = int(input("Enter the age of the Vehicle : "))
vInsurance = 0

print("The Price is : ",vPrice);
print("The Age is : ",Vage);

if Vage < 5:
    vInsurance = vPrice * 0.05
    print("Insurance Premium is : ",vInsurance)
elif Vage >= 5 and Vage <= 10:
    vInsurance = vPrice * 0.07
    print("Insurance Premium is : ",vInsurance)
elif Vage > 10:
    vInsurance = vPrice * 0.1
    print("Insurance Premium is : ",vInsurance)
else:
    print("Enter Valid Age")
