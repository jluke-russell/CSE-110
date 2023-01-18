"""
Luke Russell 
Name Age checkpoint
3/23/21
"""
people = [
    "Stephanie 36",
    "John 29",
    "Emily 24",
    "Gretchen 54",
    "Noah 12",
    "Penelope 32",
    "Michael 2",
    "Jacob 10"]
youngest = 999 
smallest_name = ""
for i in people: 
    line = i.split(" ")
    name = line[0]
    age = int(line[1])
    if youngest > age:
        youngest = age
        smallest_name = name
print(f"{smallest_name} is the youngest at {youngest} years old.")