"""
Luke Russell
Spanish Flu Milestone
3/20/21
"""

small = 1000
small_year = 100
small_country = ""
big = 0 
big_year = -1
big_country = ""

userHighExp = -1
userLowExp = 1000
userHighCountry = ""
userLowCountry = ""

numYears = 0
average = 0 

i = 0

userYear = int(input("Please input a year between 1000 and 2019: "))
with open ("life-expectancy.csv") as life:
   for line in life:
      i = i + 1
      line = line.strip() 
      parts = line.split(",")
      if i > 1:
         country = parts[0]
         code = parts[1]
         year = int(parts[2])
         expectancy = float(parts[3])
         if small > float(parts[3]):
            small = float(parts[3]) 
            small_year = parts[2]
            small_country = parts[0]
         if big < float(parts[3]):
            big = float(parts[3])
            big_year = parts[2]
            big_country = parts[0]        
         if userYear == year:
            print(f"{year} - {country} - {expectancy}")
            average = average + expectancy
            numYears = numYears + 1
            if userLowExp > float(parts[3]):
               userLowExp = float(parts[3])
               userLowCountry = parts[0]
            if userHighExp < float(parts[3]):
               userHighExp = float(parts[3])
               userHighCountry = parts[0]


print(f"The minimum life expectancy is: {small} from {small_country} in {small_year}.")
print(f"The maximum life expectancy is: {big} from {big_country} in {big_year}.")
print(f"For the year {userYear}: ")
average = average / numYears
print(f"The average life expectancy across all countries was {average:.3f}.")
print(f"The maximum life expectancy was in {userHighCountry} with {userHighExp:.3f}.")
print(f"The minimum life expectancy was in {userLowCountry} with {userLowExp:.3f}.")