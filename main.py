import pandas

data=pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
grey_count= len(data[data["Primary Fur Color"] == "Gray"])
Cinnamon_count= len(data[data["Primary Fur Color"] == "Cinnamon"])
Black_count= len(data[data["Primary Fur Color"] == "Black"])
print(grey_count)
print(Cinnamon_count)
print(Black_count)

data_dict={
      "Fur Color": ["gray","Cinnamon","Black"],
       "Count": [grey_count,Cinnamon_count,Black_count]

}

df=pandas.DataFrame(data_dict)
df.to_csv("squirrel_count.csv")