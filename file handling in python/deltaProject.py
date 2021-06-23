import csv
import os

if os.path.exists("usagedata.csv"):
    pass
else:
    file = open("usagedata.csv", "x")

with open("usagedata.csv","r") as csv_file:
    csv_reader = csv.reader(csv_file)
