import pandas

data_raw  = pandas.read_csv("PythonCoding_100days/Squirrel_06/2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

#sprint(data_raw)

data = data_raw["Primary Fur Color"]
#print(data)

nbr_grey     = data[data == "Gray"].count()
nbr_black    = data[data == "Black"].count()
nbr_cinnamon = data[data == "Cinnamon"].count()

data_dict = {"Fur Color": ["Gray","Black","Cinnamon"],"Count":[nbr_grey,nbr_black,nbr_cinnamon]}
print(data_dict)

data_frame = pandas.DataFrame(data_dict)
data_frame.to_csv("PythonCoding_100days/Squirrel_06/data_FurColor")


print(nbr_grey)

