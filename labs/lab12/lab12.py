import json

class Forecast:

    def __init__(self, name, rainfall, temperature):
        self.name = name
        self.rainfall = rainfall
        self.temperature = temperature

    def printForecast(self):
        print("City: " + self.name + " Rainfall: " + str(self.rainfall)+ " Temperature: " + str(self.temperature))

# Read in the file
dataFile = open("data.json", "r")

# Use the json module to convert the string read from the file into a dictionary
dataDict = json.load(dataFile)

# Create city objects from each of the entries and store them into a list
cities = []

for city in dataDict:
    cities.append(Forecast(city, dataDict[city][1], dataDict[city][0]))

# The city with the maximum temperature
max_temp = cities[0]

for city in cities:
    if (city.temperature > max_temp.temperature):
        max_temp = city

# The city with the minimum temperature
min_temp = cities[0]

for city in cities:
    if (city.temperature < min_temp.temperature):
        min_temp = city

# The average rainfall
sum_rainfall = 0

for city in cities:
    sum_rainfall += city.rainfall

average_rainfall = sum_rainfall / len(cities)

# Print out the name of the maximum and minimum cities, along with their forecast
max_temp.printForecast()
min_temp.printForecast()

# Print out the average rainfall
print(average_rainfall)
