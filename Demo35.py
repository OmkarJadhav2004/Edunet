#iris csv(comma seprated values)

#pair plot
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data_frame = pd.read_csv("iris.csv")
data_frame.head(3)

df = pd.DataFrame(data_frame)

sns.pairplot(df)
plt.show()

#box plot
sns.boxplot(data=df)

plt.title('Distribution of Energy Consumption by Source')
plt.show()


#Violin plot
sns.violinplot(data=df)

plt.title("Violin plot of Energy Consumption Distribution")
plt.show()

#Heatmap
numeric_data = data_frame.select_dtypes(include=["number"])
correlation_matrix = numeric_data.corr()
plt.figure(figsize=(8,6))
sns.heatmap(correlation_matrix, annot=True, cmap="coolwarm", linewidths=0.5, fmt=".2f")
plt.title("Heatmap of Feature Correlations", fontsize=14)
plt.show()
