#Pandas Library (Creating DataFrame)
#Feature Engineering

import pandas as pd

# Sample renewable energy sources data
renewable_sources = ["Solar", "Wind", "Hydropower", "Geothermal", "Biomass"]

# Sample green technology project data (for DataFrame)
data = {
    "Project": ["Solar Farm A", "Wind Turbine X", "Hydropower Y", "Solar Roof Z", "Geothermal Plant P"],
    "Technology": ["Solar", "Wind", "Hydropower", "Solar", "Geothermal"],
    "Capacity (MW)": [150, 300, 200, 50, 100],  # Megawatts
    "Cost (Million $)": [200, 400, 350, 100, 250],  # Project cost
    "Location": ["California", "Texas", "Washington", "Nevada", "Idaho"],
    "Completion Year": [2023, 2024, 2022, 2025, 2023]
}

project_df = pd.DataFrame(data)

print("\nGreen Technology Projects Dataframe:")
print(project_df)

print(project_df.iloc[2:4])

high_capacity_project = project_df[project_df["Capacity (MW)"] > 100]

print("\nProjects with Capacity Greater than 100 MW :")
print(high_capacity_project)

project_df['Cost/Capacity'] = [1.333,1.333,1.75,2,2.5]
print(project_df)

print(project_df.shape)
print(project_df.isnull().sum())

#Aggregation
total_capacity = project_df["Capacity (MW)"].sum()
total_cost = project_df["Cost (Million $)"].sum()

print("\nTotal Capacity : ",total_capacity)
print("\nTotal Cost : ",total_cost)

#Group By
grouped_data = project_df.groupby("Technology")["Capacity (MW)"].sum()

print("\nTotal Capacity by Technology")
print(grouped_data)

#info about data
print(project_df.info())

#basic stats about data
print(project_df.describe())

