#Encoding example 2 (label encoding)

from sklearn.preprocessing import LabelEncoder

import pandas as pd
import numpy as np

data = {
    "Energy Source": ["Solar", "Wind", "Hydropower", "Geothermal", "Biomass", "Nuclear"],
    "Energy Consumption (MWh)": [1200, np.nan, 2900, np.nan, 2500, 3200],
    "Cost (Million $)": [200, 400, np.nan, 150, 250, np.nan]
}

label_encoder = LabelEncoder()
data["Energy Source"] = label_encoder.fit_transform(data["Energy Source"])

print("Data after label encoding")
print(data)