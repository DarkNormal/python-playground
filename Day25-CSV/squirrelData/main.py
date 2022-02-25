# import csv
#
# if __name__ == "__main__":
#     with open("weather_data.csv", mode="r") as weatherData:
#         csvData = csv.reader(weatherData)
#         temperatures = []
#         count = 0
#         for row in csvData:
#             print(row)
#             if count > 0:
#                 temperatures.append(int(row[1]))
#             count += 1
#         print(temperatures)

import pandas

FAHRENHEIT_CONVERSION_RATE = 1.8
FAHRENHEIT_CONVERSION_CONSTANT = 32

if __name__ == "__main__":

    squirrel_data = pandas.read_csv("squirrelData/2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
    color_counts = squirrel_data["Primary Fur Color"].unique()
    print(color_counts)

    count = squirrel_data.groupby(["Primary Fur Color"]).size().reset_index(name="Count")
    count.to_csv("squirrelData/squirrel_count.csv")


    # data = pandas.read_csv("weather_data.csv")
    # print(data)
    # temperatures = data["temp"].tolist()
    # average_temp = sum(temperatures) / len(temperatures)
    # print(average_temp)
    #
    # max_temp = data["temp"].max()
    # print(max_temp)
    #
    # max_temp_row = data[data.temp == max_temp]
    # print(max_temp_row)
    #
    # monday = data[data.day == "Monday"]
    # monday_temp = int(monday.temp)
    # print(f"Monday temp: {monday_temp} celsius")
    # temp_fahrenheit = (monday_temp * FAHRENHEIT_CONVERSION_RATE) + FAHRENHEIT_CONVERSION_CONSTANT;
    # print(f"Monday temp: {temp_fahrenheit} fahrenheit")
