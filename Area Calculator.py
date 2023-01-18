"""
Luke Russell
Area Calculator
1/21/2021
"""
print('Welcome to Area Calculator!')
def main():
        shape = input("What shape do you want to calculate area for: Circle, Square, or Rectangle? ")
        
        if shape == "Circle":
            
            radius = float(input('What is the radius of the circle? '))
            area_c = 3.14 * (radius ** 2) 
            print(f'The area of the circle is {area_c:.3f}.')

        if shape == "Square":
           
            side = float(input('What is the length of the side? '))
            area_s = side * 2 
            print(f'The area of the square is {area_s:.3f}.')

        if shape == "Rectangle":
           
            length = float(input('What is the length? '))
            width = float(input('What is the width? '))
            area_r = length * width
            print(f'The area of the rectangle is {area_r:.3f}.')
main()
        
         