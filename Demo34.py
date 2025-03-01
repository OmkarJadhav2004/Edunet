#Data Visualization using seaborn

#pairplot
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

data = {
    "Solar": [1200, 1500, 1300],
    "Wind": [3400, 3600, 3200],
    "Hydropower": [2900, 3100, 2800],
    "Biomass": [2500, 2700, 2400]
}

df = pd.DataFrame(data)

sns.pairplot(df)
plt.show()

#Heatmap
correlation_matrix = df.corr()
sns.heatmap(correlation_matrix, annot = True, cmap = 'coolwarm', linewidths = 0.5)

plt.title('Correlation Between Energy Sources')
plt.show()

#Box plot
sns.boxplot(data=df)

plt.title('Distribution of Energy Consumption by Source')
plt.show()

#Violin plot
sns.violinplot(data=df)

plt.title("Violin plot of Energy Consumption Distribution")
plt.show()