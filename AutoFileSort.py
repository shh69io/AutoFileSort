import os
import shutil # Simplified the process of moving files.  
import random


# Input Directory, and Path: 
while True: 

	inputDirectory = input("Enter the name of the directory to be sorted: ")

	if inputDirectory.strip() != "":
		if os.path.exists(inputDirectory) and os.path.isdir(inputDirectory):
			inputPath = os.path.abspath(inputDirectory)
			print(f"Path Found: {inputPath}")
			break
		else:
			print("Directory not found. Try again... \n")
	else:
		print("Directory names may not be invalid. Try again...")


# Making the output direcotries: 
dirs = ['documents', 'images', 'audio', 'video']

outputPath = "output"
if not os.path.exists(outputPath):
    os.makedirs(outputPath)

for dirName in dirs:
    dirPath = os.path.join(outputPath, dirName)
    if not os.path.exists(dirPath):
        os.makedirs(dirPath)

# Random Identifier for logs: 
randStr = ""
for i in range(6):
	randStr += str(random.randint(0,6))

# Moving the files: 
extensionMap = {'documents': ['.txt', '.pdf', '.docx'],
				'images': ['.jpg', '.png', '.jpeg'],
				'audio': ['.mp3', '.wav'],
				'video': ['.mp4', '.mkv', '.avi']}

for fileName in os.listdir(inputPath):
    fileExtension = os.path.splitext(fileName)[1].lower()

    for category, extensions in extensionMap.items():

        if fileExtension in extensions:
            src = os.path.join(inputPath, fileName)
            desDir = os.path.join(outputPath, category)
            des = os.path.join(desDir, fileName)

            # Handle duplicate filenames: 
            if os.path.exists(des):
                base, ext = os.path.splitext(fileName)
                counter = 1
                while os.path.exists(des):
                    des = os.path.join(desDir, f"{base}_{counter}{ext}")
                    counter += 1

            shutil.move(src, des)

            with open(f"log{randStr}.txt", "a") as file:
                file.write(f"Moved {fileName} to output/{category}. \n")