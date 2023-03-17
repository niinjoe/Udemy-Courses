# with open("weather_data.csv") as data:
#     data_list = data.readlines()
#     print(data_list)

import csv

with open("weather_data.csv") as data_file:
    data = csv.reader(data_file)
    temperatures = []
    for row in data:
        temperatures.append(row[1])
    
    temperatures.remove(temperatures[0])
    new_temp_ls = list(map(int, temperatures))
    print(new_temp_ls)