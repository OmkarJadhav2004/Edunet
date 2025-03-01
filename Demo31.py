#Data Encoding Categorical Variables

import pandas as pd
import numpy as np

data = {
    "Energy Source": ["Solar", "Wind", "Hydropower", "Geothermal", "Biomass", "Nuclear"],
    "Energy Consumption (MWh)": [1200, np.nan, 2900, np.nan, 2500, 3200],
    "Cost (Million $)": [200, 400, np.nan, 150, 250, np.nan]
}
energy_df = pd.DataFrame(data)

energy_encoded_df = pd.get_dummies(energy_df, columns=["Energy Source"])

print("\nData After One-Hot Encoding Categorical Variables:")
print(energy_encoded_df)