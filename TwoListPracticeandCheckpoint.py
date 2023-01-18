"""
Luke Russell
Practice and Check Point
3/9/21
"""
"""
team_city = ["Salt Lake City", "Denver", "Philadelphia", "Phoenix", "Los Angeles", "New York","Toronto","Washington","Indiana","San Antonio","Charlotte", "Chicago","Golden State"]
team_name = ["Jazz", "Nuggets", "76ers", "Suns", "Lakers","Knicks", "Raptors","Wizards","Pacers","Spurs","Hornets","Bulls","Warriors"]
rankings = [1,6,1,2,3,5,8,12,10,7,7,9]
team_conference = [0,0,1,0,0,1,1,1,1,0,1,1,0]
team_division = [0,0,1,2,2,1,1,3,4,5,3,4,2]
conferences = ["West", "East"] 
divisions = ["NW", "AC", "PAC", "SE","CEN","SW"]

for i in range(0,len(team_city)):
    if divisions[team_division[i]] == "AC":
        print(f"{team_city[i]:25} {team_name[i]:15} {rankings[i]:2} {team_division[i]:5}")
"""
print("Please enter the items into the list and type 'quit' to finish: ")
shopping_list = []
item = None
while item != "quit":
    item = input("Item: ")
    if item != "quit":
        shopping_list.append(item)
print("The shopping list is: ")
for item in shopping_list:
    print(item)
print("Numbered shopping list is: ")
for i in range(len(shopping_list)):
    item = shopping_list[i]
    print(f'{i}.{item}')
print()
index = int(input("Which number item do you want to change? "))
new_item = input("What is the new item? ")

shopping_list[index] = new_item

print("The new numbered shopping list is: ")
for i in range (len(shopping_list)):
    item = shopping_list[i]
    print(f"{i}. {item}")
    