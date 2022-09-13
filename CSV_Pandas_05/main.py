import pandas
import os

path_curr_folder = os.path.dirname(os.path.abspath(__file__))
path_curr_file   = path_curr_folder + "/weather_data.csv"
data = pandas.read_csv(path_curr_file)

data_dict = data.to_dict()
print(data_dict)

temp_list = data["temp"].to_list()
print(len(temp_list))

avg_temp = data["temp"].mean()

print(data[data.day == "Monday"])


check = data[data.day == "Monday"]
print(check.temp.values)