"""
Luke Russell
List Practice 
3/2/21
"""
"""
stuff = ["five",5,"thirty-two",32,"sixty-seven",67,"eighteen",18]
for i in range(0,len(stuff),1): 
    print(stuff[1])
"""

friends = []
name = None #initalize the "name" variable 
while name != "end":
    name = input("type the name of a friend: ")
    if name != "end":
        friends.append(name)
print()
print("Your friends are:")

for friend in friends:
    print(friend)
