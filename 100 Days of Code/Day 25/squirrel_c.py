import pandas as pd

df = pd.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

black = len(df[df["Primary Fur Color"] == "Black"])

red = len(df[df["Primary Fur Color"] == "Cinnamon"])

gray = len(df[df["Primary Fur Color"] == "Gray"])

data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [gray, red, black]
}

dict_df = pd.DataFrame(data_dict)

dict_df.to_csv("squirrel_data.csv")