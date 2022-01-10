import math

import csv
with open('data.csv', newline='') as f:
    reader = csv.reader(f)
    fileData = list(reader)

data=fileData[0]

def mean(data):
    num = len(data)
    total=0
    for x in data:
        total+=int(x)
    mean = total/num
    return mean
    

square = []
for num in data:
    m = int(num)-mean(data)
    m = m **2 
    square.append(m)

sum = 0
for i in square:
    sum= sum +i

result = sum/(len(data)-1)

sd = math.sqrt(result)
print(sd)