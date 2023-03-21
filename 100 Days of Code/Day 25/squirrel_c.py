import pandas as pd

df = pd.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

black = df[df["Primary Fur Color"] == "Black"]
black_c = black["Primary Fur Color"].count()

red = df[df["Primary Fur Color"] == "Cinnamon"]
red_c = red["Primary Fur Color"].count()

gray = df[df["Primary Fur Color"] == "Gray"]
gray_c = gray["Primary Fur Color"].count()

black.to_csv("test.csv")

