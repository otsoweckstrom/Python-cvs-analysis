import csv
import datetime
import time

# importing csv module

# csv file name
filename = "Rawdata.csv"
order_dates = []
delivery_dates = []
yearly_average_time = datetime.timedelta()

# reading csv file
with open(filename, 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    next(csvreader)
    content = csv.reader(csvfile, delimiter=';')

    # Changing the dates to actual dates instead of text :)
    for row in content:
        order_date = datetime.datetime.strptime(
            row[0], "%d.%m.%Y %H.%M.%S")
        order_dates.append(order_date)

        delivery_date = datetime.datetime.strptime(
            row[1], "%d.%m.%Y %H.%M.%S")
        delivery_dates.append(delivery_date)

        shipping_date = datetime.datetime.strptime(
            row[2], "%d.%m.%Y %H.%M.%S")


for i in range(len(order_dates)):
    temp_average_time = delivery_dates[i] - order_dates[i]
    yearly_average_time = yearly_average_time + temp_average_time


average_delivery_time = yearly_average_time / len(order_dates)
print(average_delivery_time)
