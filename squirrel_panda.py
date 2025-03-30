import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

Gray_count = len(data[data["Primary Fur Color"]=="Gray"])

Cinnamon_count=len(data[data["Primary Fur Color"]=="Cinnamon"])

Black_count=len(data[data["Primary Fur Color"]=="Black"])

print(Gray_count)

print(Cinnamon_count)

print(Black_count)

data_to_dict={

    "Fur Color":["Gray","Cinnamon","Black"],

    "Count":["2473","392","103"]

}

df=pandas.DataFrame(data_to_dict)

df.to_csv("Squirrel_Dict.csv")