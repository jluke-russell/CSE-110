""" 
Luke Russell 
Milestone Pics
2/20/21
"""
"""
# Part 1 
from PIL import Image
#print('The library is loaded correctly.')

desert_image = Image.open("desert.jpg")
width, height = desert_image.size
print(desert_image.size)

pixels_original = desert_image.load()
r, g, b = pixels_original[100,200]
pixels_original[100,200] = (r, g, b)
print(pixels_original[100,200])
pixels_original[100,200] = (255, 0, 0)

pixels_original1 = desert_image.load()
r, g, b = pixels_original1[50,50]
pixels_original1[50,50] = (r, g, b)
print(pixels_original1[50,50])
pixels_original1[50,50] = (255, 0, 0)

pixels_original = desert_image.load()
r, g, b = pixels_original[200,200]
pixels_original[200,200] = (r, g, b)
print(pixels_original[200,200])
pixels_original[200,200] = (255, 0, 0)

pixels_original = desert_image.load()
r, g, b = pixels_original[100,100]
pixels_original[100,100] = (r, g, b)
print(pixels_original[100,100])
pixels_original[100,100] = (255, 0, 0)

pixels_original = desert_image.load()
r, g, b = pixels_original[10,200]
pixels_original[10,200] = (r, g, b)
print(pixels_original[10,200])
pixels_original[10,200] = (255, 0, 0)

desert_image.show()
""" 

"""
#Part 2 
from PIL import Image
image_boat = Image.open("boat.jpg")
pixels_boat = image_boat.load()
image_sunset = Image.open("sunset.jpg")
pixels_sunset = image_sunset.load()
print(image_boat.size)
print(image_sunset.size)
new_image = image_sunset.size
pic_neo = Image.new("RGB", new_image)
pixels_new_image = pic_neo.load()

for row in range(new_image[1]):
    for column in range(new_image[0]):
        (r,g,b) = pixels_boat[column,row]
        if g>28 and r < 300 and b <300:
            (r,g,b) = pixels_sunset[column,row]
        
        pixels_new_image[column,row] = (r,g,b)
pic_neo.show()
pic_neo.save("BoatAtSunset.jpg")

image_shuttle = Image.open("spaceshuttle.jpg")
pixels_shuttle = image_shuttle.load()
image_earth = Image.open("earth.jpg")
pixels_earth = image_earth.load()
print(image_shuttle.size)
print(image_earth.size)
new_image1 = image_earth.size
pic_neo1 = Image.new("RGB", new_image1)
pixels_new_image1 = pic_neo1.load()

for row in range(new_image1[1]):
    for column in range(new_image1[0]):
        (r,g,b) = pixels_shuttle[column,row]
        if g> 110 and r <110 and b <110:
            (r,g,b) = pixels_earth[column,row]
        
        pixels_new_image1[column,row] = (r,g,b)
pic_neo1.show()
pic_neo1.save("InOrbit.jpg")

image_penguin = Image.open("penguin.jpg")
pixels_penguin = image_penguin.load()
image_forest = Image.open("forest.jpg")
pixels_forest = image_forest.load()
print(image_penguin.size)
print(image_forest.size)
new_image2 = image_forest.size
pic_neo2 = Image.new("RGB", new_image2)
pixels_new_image2 = pic_neo2.load()

for row in range(new_image2[1]):
    for column in range(new_image2[0]):
        (r,g,b) = pixels_penguin[column,row]
        if g>105 and r < 105 and b <105:
            (r,g,b) = pixels_forest[column,row]
        
        pixels_new_image2[column,row] = (r,g,b)
pic_neo2.show()
pic_neo2.save("lostpenguin.jpg")

image_cactus = Image.open("cactus.jpg")
pixels_cactus = image_cactus.load()
image_snowscape = Image.open("snowscape.jpg")
pixels_snowscape = image_snowscape.load()
print(image_cactus.size)
print(image_snowscape.size)
new_image3 = image_snowscape.size
pic_neo3 = Image.new("RGB", new_image3)
pixels_new_image3 = pic_neo3.load()

for row in range(new_image3[1]):
    for column in range(new_image3[0]):
        (r,g,b) = pixels_cactus[column,row]
        if g>115 and r < 115 and b <115:
            (r,g,b) = pixels_snowscape[column,row]
        
        pixels_new_image3[column,row] = (r,g,b)
pic_neo3.show()
pic_neo3.save("WhiteDesert.jpg")
"""

from PIL import Image
image_hiker = Image.open("hiker.jpg")
pixels_hiker = image_hiker.load()
image_SD70ACe = Image.open("SD70ACe.jpg")
pixels_SD70ACe = image_SD70ACe.load()
print(image_hiker.size)
print(image_SD70ACe.size)
new_image4 = image_SD70ACe.size
pic_neo4 = Image.new("RGB", new_image4)
pixels_new_image4 = pic_neo4.load()

for row in range(new_image4[1]):
    for column in range(new_image4[0]):
        (r,g,b) = pixels_hiker[column,row]
        if g>115 and r < 115 and b <115:
            (r,g,b) = pixels_SD70ACe[column,row]
        
        pixels_new_image4[column,row] = (r,g,b)
pic_neo4.show()
pic_neo4.save("RailFanning.jpg")