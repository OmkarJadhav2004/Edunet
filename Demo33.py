#Data Visualization using matplotlib

#Line Plot
import matplotlib.pyplot as plt
# months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']
# cost = [200, 400, 300, 150, 250, 200]
energy_consumption = [1200, 1300, 1100, 1500, 1400, 1600]
energy_sources = ["Solar", "Wind", "Hydropower", "Geothermal", "Biomass", "Nuclear"]

plt.plot(energy_consumption, energy_sources, marker='o', color='b', linestyle='--')

plt.title('Energy Consumption Over 6 Months')
plt.xlabel('Consumption MWh')
plt.ylabel('Energy Sources')
plt.show()

#Bar Chart
energy_sources = ['Solar', 'Wind', 'Hydropower', 'Biomass']
energy_values = [1200, 3400, 2900, 2500]

plt.bar(energy_sources, energy_values, color='green')

plt.title('Energy Consumption by Renewable Energy Source')
plt.xlabel('Energy Source')
plt.ylabel('Energy Consumption (MWh)')
plt.show()

#Pie Chart
plt.pie(energy_values, labels=energy_sources, autopct='%1.1f%%', colors=['gold', 'lightblue', 'lightgreen', 'coral'])

plt.title('Energy Consumption Share by Source')
plt.show()

#Scatter Plot
cost = [200, 400, 300, 150, 250, 200]
energy_consumption = [1200, 1300, 1100, 1500, 1400, 1600]

plt.scatter(energy_consumption, cost, color='red')

plt.title('Energy Consumption vs Cost')
plt.xlabel('Energy Consumption (MWh)')
plt.ylabel('Cost (Million $)')
plt.show()