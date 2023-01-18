"""
Luke Russell
Class Data 
3/16/21
"""
counter = 0 
with open("Classroom Info.csv") as class_file:
    for line in class_file:
        clean_line = line.strip()
        columns = clean_line.split(",")
        if columns[0] == "Name":
            pass # This skips over the above if statement
        else:
            counter += 1 
            print(f"Row {counter}")
            print(f"{columns[0]} has lived in {columns[2]} cities, and their favorite color is {columns[1]}.")
        