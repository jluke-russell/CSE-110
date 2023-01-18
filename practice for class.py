""" 
Checkpoint and practice for class
2/23/21
"""

for color in["red", "blue","green","yellow"]:
    print(color)
for num in[1,2,3,4,5,6,7,8]: 
    print(num)
for num1 in range(1,9):
    print(num1)
for number in range(2,22,2):
    print(number)


"""
for i in[0,1,2,21,69,420]:
    print('what is 9 + 10?')
    print(i)
"""
"""
for a in range(20,-1,-1):
    print('what is 9 + 10?')
    print(a)
"""
"""
from PIL import Image

earth_image = Image.open("earth.jpg")
earth_pixels = earth_image.load()
width, height = earth_image.size
print(earth_image.size)
print(earth_pixels[600,500])
"""
"""
for q in range(600):
    earth_pixels[600, q]=(225,0,0)
for q in range(800):
    earth_pixels[q, 500]=(225,0,0)
earth_image.show()
"""
"""
for row in range (600): 
    for column in range (500):
        earth_pixels[column,row]=(72,93,100)
        earth_image.show()
"""        
