#sklearn library
#Normalization or Scaling

#MinMax Scaler
from sklearn.preprocessing import MinMaxScaler
import pandas as pd
import numpy as np

data = {
    "Energy Source": ["Solar", "Wind", "Hydropower", "Geothermal", "Biomass", "Nuclear"],
    "Energy Consumption (MWh)": [1200, np.nan, 2900, np.nan, 2500, 3200],
    "Cost (Million $)": [200, 400, np.nan, 150, 250, np.nan]
}

energy_df = pd.DataFrame(data)

scaler = MinMaxScaler()
energy_df[["Energy Consumption (MWh)", "Cost (Million $)"]] = scaler.fit_transform(energy_df[["Energy Consumption (MWh)", "Cost (Million $)"]])
print(energy_df)

#Standard Scaler(z-score scaling)
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
energy_df[["Energy Consumption (MWh)", "Cost (Million $)"]] = scaler.fit_transform(
    energy_df[["Energy Consumption (MWh)", "Cost (Million $)"]]
)

print("\nData After Standardization (Z-score Scaling):")
print(energy_df)

