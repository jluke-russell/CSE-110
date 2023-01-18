"""
Luke Russell
Reveiw 
3/30/21
"""
names = []
colors = []

color = "Invalid"
name = ""

def process(place_1, place_2):
    judgement = True
    if place_1 != "x" and place_2 == "blue":
        judgement = False
    return judgement


while name != "quit":
    name = input("What is your name? ")
    if name != "quit":
        color = input(f"What is {name}\'s favorite color? ")
        colors.append(color)
        names.append(name)
for i in range(len(names)): 
    if process(names[i], colors[i]):
        print(f"{names[i]}\'s favorite color is {colors[i]}.")
    else: 
        print(f"{names[i]}\'s favorite color is {colors[i]} and was judged falsely.")
