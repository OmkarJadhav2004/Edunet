#carbon footprint check

carbon_footprint = 500.75

print(f"Carbon Footprint : {carbon_footprint} kg Co2")

is_sustainable = carbon_footprint < 400
print(f"Is city sustainable? : {is_sustainable}")

#Temprature list

weekly_templist = [25,27,28,26,24,30,29]

print(f"Weekly Tempratures : {weekly_templist}")

#temp values more than 25 degree celcius

for i in range(0,7):
    if weekly_templist[i] > 25:
        print(weekly_templist[i], end=" ")


# create dictionary variable to store city data
city_data ={"name": "City A","temprature":25,"carbon_footprint":500.75,"is_sustainable":False}
print("City data : ",city_data)

print(city_data["temprature"])
print(city_data.keys())
print(city_data.values())

city_data["AQI"] = 100
print(city_data)

#remove value from templist

weekly_templist.remove(26)
print("Updated Weekly Temprature list : ",weekly_templist)

#pop
weekly_templist.pop()
print("Updated Weekly Temprature list : ",weekly_templist)

#append
weekly_templist.append(29)
print("Updated Weekly Temprature list : ",weekly_templist)


nlist1 = ['mon','tue','wed','thu']
weekly_templist.extend(nlist1)
print("Updated Weekly Temprature list : ",weekly_templist)

