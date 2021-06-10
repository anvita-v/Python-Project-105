import csv
import math


with open('data.csv', newline = '') as f:
    reader = csv.reader(f)
    file_data = list(reader)

#file_data.pop(0)

data = file_data[0]

def mean(data):
    n = len(data)
    total = 0
    for x in data:
        total += int(x)
    
    mean = total/n
    return mean

squared_list = []
for number in data:
    a = int(number) - mean(data)
    a = a**2
    squared_list.append(a)

#calculating sum
sum = 0
for i in squared_list:
    sum = sum + i
#dividing sum by total values
result = sum/(len(data)-1)

#square root of result
std_dev = math.sqrt(result)

print(std_dev)

