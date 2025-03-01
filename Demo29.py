#Missing data

import pandas as pd
import numpy as np

data = {
    "Energy Source": ["Solar", "Wind", "Hydropower", "Geothermal", "Biomass", "Nuclear"],
    "Energy Consumption (MWh)": [1200, np.nan, 2900, np.nan, 2500, 3200],
    "Cost (Million $)": [200, 400, np.nan, 150, 250, np.nan]
}

energy_df = pd.DataFrame(data)

print("Original Energy data with missing values:")
print(energy_df)

print(energy_df.isnull().sum())

cleaned_df1 = energy_df.dropna()

print("\nData After Removing Rows with missing Values")
print(cleaned_df1)


#replace missing values with mean values
ec_m = energy_df["Energy Consumption (MWh)"].mean()
c_m = energy_df["Cost (Million $)"].mean()
print("Mean of Energy Consumption : ",ec_m)
print("Mean of Cost:",c_m)

energy_df["Energy Consumption (MWh)"].fillna(ec_m,inplace = True)
energy_df["Cost (Million $)"].fillna(c_m,inplace = True)

print("\nDta After Inputting Missing Values with Mean:")
print(energy_df)

#Forward Fill
data = {
    "Energy Source": ["Solar", "Wind", "Hydropower", "Geothermal", "Biomass", "Nuclear"],
    "Energy Consumption (MWh)": [1200, np.nan, 2900, np.nan, 2500, 3200],
    "Cost (Million $)": [200, 400, np.nan, 150, 250, np.nan]
}

energy_df = pd.DataFrame(data)

print("Original Energy data with missing values:")
print(energy_df)
forward_filled_df = energy_df.fillna(method="ffill")

print("\nData After Forward Filling:")
print(forward_filled_df)

'''
    //BackWard Fill
'''


