""" 
Luke Russell 
Milestone Pics
2/20/21
"""
from PIL import Image
#print('The library is loaded correctly.')

desert_image = Image.open("desert.jpg")
desert_image.show()
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