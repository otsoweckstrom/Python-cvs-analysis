import csv
import datetime
import time

# importing csv module

# csv file name
filename = "Rawdata.csv"
start_time = time.time()
order_dates_itemLabel = []
order_dates_noItemLabel = []
order_dates_extraPackaging = []
d_dates_label = []
d_dates_noLabel = []
d_dates_extra = []
y_avg_time_extra = datetime.timedelta()
y_avg_time_noLabel = datetime.timedelta()
y_avg_time_label = datetime.timedelta()
Keyword = "ExtraPacking"
Keyword_2 = "NoItemLabel"
Keyword_3 = "ItemLabel"

extraPackaging_rows = []
noItemLabel_rows = []
itemLabel_rows = []

# reading csv file
with open(filename, 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    next(csvreader)
    content = csv.reader(csvfile, delimiter=";")
    # Splitting rows into different categories
    for row in content:

        if Keyword in row[5]:
            extraPackaging_rows.append(row)
        elif Keyword_2 in row[5]:
            noItemLabel_rows.append(row)
        elif Keyword_3 in row[5]:
            itemLabel_rows.append(row)

    # Changing the dates to actual dates instead of text :)
    for row in extraPackaging_rows:
        order_date_extraPackaging = datetime.datetime.strptime(
            row[0], "%d.%m.%Y %H.%M.%S")
        order_dates_extraPackaging.append(order_date_extraPackaging)

        delivery_date_extraPackaging = datetime.datetime.strptime(
            row[1], "%d.%m.%Y %H.%M.%S")
        d_dates_extra.append(delivery_date_extraPackaging)

        shipping_date_extraPackaging = datetime.datetime.strptime(
            row[2], "%d.%m.%Y %H.%M.%S")

    for row in noItemLabel_rows:
        order_date_noitemLabel = datetime.datetime.strptime(
            row[0], "%d.%m.%Y %H.%M.%S")
        order_dates_noItemLabel.append(order_date_noitemLabel)

        delivery_date_noitemLabel = datetime.datetime.strptime(
            row[1], "%d.%m.%Y %H.%M.%S")
        d_dates_noLabel.append(delivery_date_noitemLabel)

        shipping_date_noitemLabel = datetime.datetime.strptime(
            row[2], "%d.%m.%Y %H.%M.%S")

    for row in itemLabel_rows:
        order_date_itemLabel = datetime.datetime.strptime(
            row[0], "%d.%m.%Y %H.%M.%S")
        order_dates_itemLabel.append(order_date_itemLabel)

        d_date_itemLabel = datetime.datetime.strptime(
            row[1], "%d.%m.%Y %H.%M.%S")
        d_dates_label.append(d_date_itemLabel)

        shipping_date_itemLabel = datetime.datetime.strptime(
            row[2], "%d.%m.%Y %H.%M.%S")


for i in range(len(order_dates_extraPackaging)):
    temp_avg_time_extra = d_dates_extra[i] - order_dates_extraPackaging[i]
    y_avg_time_extra = y_avg_time_extra + temp_avg_time_extra

for i in range(len(order_dates_noItemLabel)):
    temp_avg_time_noLabel = d_dates_noLabel[i] - order_dates_noItemLabel[i]
    y_avg_time_noLabel = y_avg_time_noLabel + temp_avg_time_noLabel

for i in range(len(order_dates_itemLabel)):
    temp_avg_time_label = d_dates_label[i] - order_dates_itemLabel[i]
    y_avg_time_label = y_avg_time_label + temp_avg_time_label


avg_deli_time_extra = y_avg_time_extra / len(order_dates_extraPackaging)
avg_deli_time_label = y_avg_time_label / len(order_dates_itemLabel)
avg_deli_time_noLabel = y_avg_time_noLabel / len(order_dates_noItemLabel)


print("Average delivery times for items with extra packaging: ",
      avg_deli_time_extra)
print("Average delivery times for items with item label: ",
      avg_deli_time_label)
print("Average delivery times for items with no item label: ",
      avg_deli_time_noLabel)
