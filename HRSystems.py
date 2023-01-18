"""
Luke Russell
Team Activity HR People 
3/18/21
"""
with open ("hr_system.txt") as system:
    for line in system:
        parts = line.split(" ")
        name = parts[0]
        id_num = parts[1]
        title = parts[2]
        salary = float(parts[3])
        print(f"Name: {name}, Title: {title}") #core
        print()
        print(f"{name}, (ID: {id_num}), {title} - ${salary:.2f}") #stretch 1
        print()
        monthly_pay = salary / 24
        print(f"{name}, (ID: {id_num}), {title} - ${monthly_pay:.2f}") #stretch 2
        if title == "Engineer":
            monthly_pay += 1000
        print(f"{name}, (ID: {id_num}), {title} - ${monthly_pay:.2f}") #stretch 3