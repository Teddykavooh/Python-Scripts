import csv

f = open("ford_escort.csv") #Open the file
csv_f = csv.reader(f) #Parse the file
"""Parsing-analzing a file's contect to correctly structure the data"""
for row in csv_f:
    name, phone, role = row
    print("Name: {}, Phone: {}, Role: {}".format(name, phone, role))
f.close()
