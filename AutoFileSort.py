import os
import shutil # Simplified the process of moving files.  
import random
from datetime import datetime


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
outputPath = "output"
if not os.path.exists(outputPath):
    os.makedirs(outputPath)



# Random Identifier for logs: 
randStr = ""
for i in range(6):
    randStr += random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789")



# Moving the files: 
extensionMap = {'documents': ['.txt', '.pdf', '.docx', '.doc', '.xls', '.ppt', '.csv', '.json', '.xml', '.odt', '.ods', '.odp'],
                'images': ['.jpg', '.png', '.jpeg', '.gif', '.bmp', '.tiff', '.svg'],
                'audio': ['.mp3', '.wav', '.aac', '.ogg', '.flac', '.wma'],
                'video': ['.mp4', '.mkv', '.avi', '.mov', '.flv', '.wmv', '.webm'],
                'archives' : ['.zip', '.rar', '.7z', '.tar', '.gz'],
                'scripts': ['.py', '.java', '.cpp', '.js', '.html', '.css', '.json', '.xml']}


for root, dirs, files in os.walk(inputPath):
    for fileName in files:
        if not fileName.startswith("."):
            fileExtension = os.path.splitext(fileName)[1].lower()

            for category, extensions in extensionMap.items():
                if fileExtension in extensions:
                    if not os.path.exists(os.path.join(outputPath, category)):
                        os.makedirs(os.path.join(outputPath, category))

                    src = os.path.join(root, fileName) 
                    desDir = os.path.join(outputPath, category)
                    des = os.path.join(desDir, fileName)

                    # Handling duplicate file names: 
                    if os.path.exists(des):
                        base, ext = os.path.splitext(fileName)
                        counter = 1
                        while os.path.exists(des):
                            des = os.path.join(desDir, f"{base}_{counter}{ext}")
                            counter += 1

                    try:
                        shutil.move(src, des)

                        print(f"Moved {fileName} from {root} to {category}")

                        with open(f"log{randStr}.txt", "a") as logFile:
                            logFile.write(f"Moved {fileName} from {root} to output/{category}      [{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}]\n")

                    except Exception as e:

                        print(f"Error moving {fileName}: {e}")

                        with open(f"log{randStr}.txt", "a") as logFile:
                            logFile.write(f"Error moving {fileName}: {e}.      [{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}]\n")

                else:
                    if not os.path.exists(os.path.join(outputPath, "unsorted")):
                        os.makedirs(os.path.join(outputPath, "unsorted"))

                    src = os.path.join(root, fileName)
                    desDir = os.path.join(outputPath, "unsorted")
                    des = os.path.join(desDir, fileName)

                    try:
                        shutil.move(src, des)

                        print(f"Moved {fileName} from {root} to unsorted")

                        with open(f"log{randStr}.txt", "a") as logFile:
                            logFile.write(f"Moved {fileName} from {root} to output/unsorted      [{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}]\n")

                    except Exception as e:

                        print(f"Error moving {fileName}: {e}")

                        with open(f"log{randStr}.txt", "a") as logFile:
                            logFile.write(f"Error moving {fileName}: {e}.      [{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}]\n")

