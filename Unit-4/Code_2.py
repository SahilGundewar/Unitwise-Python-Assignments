import csv

row_count = 0

with open("data.csv","r") as f:
    z = csv.reader(f) 
    for row in z:
        row_count += 1 
    print(row_count) 