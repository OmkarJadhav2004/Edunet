#Apply conditional statements to filter higher temprature cities

climate_data = [
    {"city": "City A", "temperature": 25, "carbon_footprint": 500},
    {"city": "City B", "temperature": 30, "carbon_footprint": 350},
    {"city": "City C", "temperature": 22, "carbon_footprint": 600},
    {"city": "City D", "temperature": 15, "carbon_footprint": 200},
    {"city": "City E", "temperature": 28, "carbon_footprint": 450}
]

for i in climate_data:
    if i['temperature'] > 25:
        print(i['city'])


#find average of carbon footprint
total = 0
avg = 0
for i in climate_data:
    total += i["carbon_footprint"]
avg = total/len(climate_data)
print(avg)