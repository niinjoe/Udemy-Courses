# with open("weather_data.csv") as data:
#     data_list = data.readlines()
#     print(data_list)

# import csv

# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         temperatures.append(row[1])

#     temperatures.remove(temperatures[0])
#     new_temp_ls = list(map(int, temperatures))
#     print(new_temp_ls)

import pandas as pd

data = pd.read_csv("weather_data.csv")

# print(data["temp"])

# data_dict = data.to_dict()
# print(data_dict)

temp_list = data["temp"].tolist()

# print(temp_list)

# My attempt for the average
avg = 0
for i in temp_list:
    avg += i
new_avg = avg / len(temp_list)
print(new_avg)

# Instructors code
average = sum(temp_list) / len(temp_list)
print(average)

#Shorter version with Pandas
print(data["temp"].mean())

#Print max value
print(data["temp"].max())

#Get data with pandas
print(data["condition"])
print(data.condition)

#Get data from a row
print(data[data["condition"] == "Sunny"])
print(data[data["day"] == "Monday"])

#Get data from the row with the max temp
max = data["temp"].max()
# print(max)
print(data[data["temp"] == max])

monday = data[data.day == "Monday"]
print(monday.condition)

#Convert from Celcius to Farenheit
def f(x):
    x = x * 1.8 + 32
    return float(x)

print(monday.temp.apply(f))