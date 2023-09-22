# # with open("weather_data.csv") as data_file:
# #     data = data_file.readlines()
# #     print(data)
#
# # import csv
# #
# # with open("weather_data.csv") as data_file:
# #     data = csv.reader(data_file)
# #     temperatures = []
# #     for row in data:
# #         if row[1] != "temp":
# #             temperatures.append(int(row[1]))
# #     print(temperatures)
#
# import pandas
#
# # Dataframe = whole table or excel sheet
# # Series is a single column in the table (like a list)
#
# data = pandas.read_csv("weather_data.csv")
#
# # # print(type(data))
# # # print(data["temp"])
# #
# # data_dict = data.to_dict()
# # print(data_dict)
# #
# # temp_list = data["temp"].tolist()
#
# # avge_temp = 0
# # for temp in temp_list:
# #     avge_temp += temp
# # avge_temp /= len(temp_list)
#
# # avge_temp = sum(temp_list) / len(temp_list)
#
# # avge_temp = data["temp"].mean()
# # max_temp = data["temp"].max()
# # print(max_temp)
#
# # Get Data In Columns
#
# #print(data["condition"])
# # print(data.condition)
#
# # Get Data in Rows
#
# # print(data[data.day == "Monday"])
# # print(data[data.temp == data.temp.max()])
# # #
# # # monday = data[data.day == "Monday"]
# # # monday_temp = monday.temp[0]
# # # print(monday_temp * 9 / 5 + 32)
# #
# # # create a dataframe from scratch
# #
# # data_dict = {
# #     "students": ["Amy", "James", "Angela"],
# #     "scores": [76, 56, 65]
# # }
# #
# # data = pandas.DataFrame(data_dict)
# # data.to_csv("new_data.csv")

import pandas
data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

gray_squirrels_count = len(data[data["Primary Fur Color"] == "Gray"])
red_squirrels_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrels_count = len(data[data["Primary Fur Color"] == "Black"])

data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [gray_squirrels_count, red_squirrels_count, black_squirrels_count]
}

df = pandas.DataFrame(data_dict)
df.to_csv("squirrel_count.csv")
