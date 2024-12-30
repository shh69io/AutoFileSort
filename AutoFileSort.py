import os
import shutil
import random
from datetime import datetime



# Input and Path: 
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



# Making the output directories:
outputPath = "output"
if not os.path.exists(outputPath):
    os.makedirs(outputPath)



# Random Identifier for logs:
randStr = "".join(random.choices("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789", k=6))



# Moving the files:
extensionMap = {
    'documents': ['.txt', '.pdf', '.docx', '.doc', '.xls', '.ppt', 'pptx', '.csv', '.json', '.xml', '.odt', '.ods', '.odp'],
    'images': ['.jpg', '.png', '.jpeg', '.gif', '.bmp', '.tiff', '.svg'],
    'audio': ['.mp3', '.wav', '.aac', '.ogg', '.flac', '.wma'],
    'video': ['.mp4', '.mkv', '.avi', '.mov', '.flv', '.wmv', '.webm'],
    'archives': ['.zip', '.rar', '.7z', '.tar', '.gz'],
    'scripts': ['.py', '.java', '.cpp', '.js', '.html', '.css', '.json', '.xml']
}


for root, dirs, files in os.walk(inputPath):
    for fileName in files:
        if not fileName.startswith("."):
            fileExtension = os.path.splitext(fileName)[1].lower()
            moved = False

            for category, extensions in extensionMap.items():
                if fileExtension in extensions:
                    categoryPath = os.path.join(outputPath, category)

                    # Ensure the destination directory exists: 
                    if not os.path.exists(categoryPath):
                        try:
                            os.makedirs(categoryPath)
                        except Exception as e:
                            print(f"Error creating category directory {categoryPath}: {e}")
                            continue

                    # Full paths: 
                    src = os.path.join(root, fileName)
                    des = os.path.join(categoryPath, fileName)

                    # Handling duplicate file names: 
                    if os.path.exists(des):
                        base, ext = os.path.splitext(fileName)
                        counter = 1
                        while os.path.exists(des):
                            des = os.path.join(categoryPath, f"{base}_{counter}{ext}")
                            counter += 1

                    try:
                        shutil.move(src, des)
                        moved = True
                        print(f"Moved {fileName} from {root} to {category}")

                        # Log the move
                        with open(f"log{randStr}.txt", "a") as logFile:
                            logFile.write(f"Moved {fileName} from {root} to output/{category}      [{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}]\n")

                    except Exception as e:
                        print(f"Error moving {fileName}: {e}")

                        # Log the error
                        with open(f"log{randStr}.txt", "a") as logFile:
                            logFile.write(f"Error moving {fileName}: {e}.      [{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}]\n")

                    break

            # If the file doesn't match any category, move it to 'unsorted': 
            if not moved:
                unsortedPath = os.path.join(outputPath, "unsorted")

                if not os.path.exists(unsortedPath):
                    try:
                        os.makedirs(unsortedPath)
                    except Exception as e:
                        print(f"Error creating unsorted directory {unsortedPath}: {e}")
                        continue  # Skip to the next file

                src = os.path.join(root, fileName)
                des = os.path.join(unsortedPath, fileName)

                try:
                    shutil.move(src, des)
                    print(f"Moved {fileName} from {root} to unsorted")

                    with open(f"log{randStr}.txt", "a") as logFile:
                        logFile.write(f"Moved {fileName} from {root} to output/unsorted      [{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}]\n")

                except Exception as e:
                    print(f"Error moving {fileName}: {e}")

                    with open(f"log{randStr}.txt", "a") as logFile:
                        logFile.write(f"Error moving {fileName}: {e}.      [{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}]\n")
