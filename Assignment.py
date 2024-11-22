import os
file = open("DataFile.txt", "r")
 
print(file.read())


writeDoc = open("DataFile.txt", "a")
writeDoc.write("This is a write test")

#Error Handling
try:
    file = open("myDataFile.txt", "r")
except FileNotFoundError:
    print("File not found")
finally:
    print("Try again")