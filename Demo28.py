#Numpy Library
#Array in python

import numpy as np

energy_consumption=np.array([1200,3400,2900,1800,2500])
print("Energy consumption (in MW) for different renuable source: ",energy_consumption)
print(type(energy_consumption))

#Total Consumption
total_consumption = np.sum(energy_consumption)
print(f"Total Energy Consumption : {total_consumption}")

#Mean Consumption
mean_consumption = np.mean(energy_consumption)
print(f"Mean Energy Consumption : {mean_consumption}")

#Standard Deviation of  Energy Consumption
std_deviation = np.std(energy_consumption)
print(f"Standard Deviation of  Energy Consumption : {std_deviation}")


#Reshaping in array
energy_consumption2 = np.array([1200,3400,2900,1800,2500,4700])
reshaped_array = energy_consumption2.reshape((3,2))

print("Reshaped Energy Consumption array is : ")
print(reshaped_array)

reshaped_array.flatten()
print("Flatten array : ",reshaped_array)

#Transpose of matrix
reshaped_array = np.array([[1200,2900,2500],[3400,1800,4700]])
print(reshaped_array)

