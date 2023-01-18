"""
Luke Russell
Books and Chapters 
3/25/21
"""

max_chap = -1 
title_with_most = ""
choose_vol = input("What volume of Scripture would you like to learn about? ")

with open("books_and_chapters.txt") as books: 
    for line in books:
        parts = line.split(":")
        title = parts[0].strip()
        chapters = int(parts[1])
        volume = parts[2].strip()
        #print(f"Scripture: {volume}, Book: {title}, Chapters: {chapters}")
        if volume.lower() == choose_vol.lower():
            print(f"Scripture: {volume}, Book: {title}, Chapters: {chapters}")
            if chapters > max_chap:
                max_chap = chapters
                title_with_most = title 
print(f"The book with the most chapters is: {title_with_most}.")
print(f"It has {max_chap} chapters.")
    if volume == "Book of Mormon":    
        print(f"Scripture: {volume}, Book: {title}, Chapters: {chapters}")
    if chapters > max_chap:
        max_chap = chapters
        title_with_most = title        
print(f"The book with the most chapters is: {title_with_most}.")
print(f"It has {max_chap} chapters.")

