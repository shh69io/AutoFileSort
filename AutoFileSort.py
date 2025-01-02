import os
import shutil   # For moving files
import random
from datetime import datetime
import json
import argparse    # For parsing CLI arguments



defaultConfig = {
    "documents": [
        ".txt", ".pdf", ".docx", ".doc", ".xls", ".xlsx", ".ppt", ".pptx", ".csv", ".json",
        ".xml", ".odt", ".ods", ".odp", ".rtf", ".epub", ".md", ".tex", ".log"
    ],
    "images": [
        ".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff", ".svg", ".ico", ".webp", ".heic", ".raw"
    ],
    "audio": [
        ".mp3", ".wav", ".aac", ".ogg", ".flac", ".wma", ".m4a", ".alac", ".opus", ".amr"
    ],
    "video": [
        ".mp4", ".mkv", ".avi", ".mov", ".flv", ".wmv", ".webm", ".m4v", ".mpeg", ".3gp"
    ],
    "archives": [
        ".zip", ".rar", ".7z", ".tar", ".gz", ".bz2", ".xz", ".iso", ".cab", ".dmg"
    ],
    "scripts": [
        ".py", ".java", ".cpp", ".c", ".js", ".ts", ".html", ".css", ".php", ".sh",
        ".bat", ".pl", ".rb", ".go", ".rs", ".swift", ".kt", ".scala", ".sql"
    ],
    "code": [
        ".cs", ".h", ".hpp", ".vb", ".asm", ".s", ".lua", ".dart", ".r", ".m",
        ".mat", ".jl", ".erl", ".ex", ".exs"
    ],
    "fonts": [
        ".ttf", ".otf", ".woff", ".woff2", ".eot"
    ],
    "design": [
        ".psd", ".ai", ".xd", ".fig", ".sketch", ".indd", ".dwg"
    ],
    "executables": [
        ".exe", ".msi", ".app", ".apk", ".bin", ".sh", ".cmd", ".deb", ".rpm"
    ],
    "database": [
        ".db", ".sql", ".sqlite", ".sqlite3", ".mdb", ".accdb"
    ],
    "3d": [
        ".obj", ".fbx", ".stl", ".dae", ".blend", ".3ds", ".gltf", ".glb"
    ],
    "unsorted": []
}




def getInputDirectory():
    while True:
        inputDirectory = input("Enter the name of the directory to be sorted: ")
        if inputDirectory.strip() != "":
            if os.path.exists(inputDirectory) and os.path.isdir(inputDirectory):
                return os.path.abspath(inputDirectory)
            else:
                print("Directory not found. Try again...\n")
        else:
            print("Directory names may not be invalid. Try again...")



def loadConfig(configFile):
    try:
        with open(configFile, 'r') as configFile:
            return json.load(configFile)

    except FileNotFoundError:
        print(f"Error: Config file '{configFile}' not found. Using default settings...")
        return defaultConfig

    except json.JSONDecodeError as e:
        print(f"Error: Invalid JSON format in '{configFile}'. {e}")
        return defaultConfig



def createOutputDirectory(path):
    if not os.path.exists(path):
        os.makedirs(path)



def moveFile(src, des, logFile):
    base, ext = os.path.splitext(os.path.basename(src))
    counter = 1

    while os.path.exists(des):
        des = os.path.join(os.path.dirname(des), f"{base}_{counter}{ext}")
        counter += 1

    try:
        shutil.move(src, des)
        logMessage = f"Moved {os.path.basename(src)} from {os.path.dirname(src)} to {os.path.dirname(des)}"

    except Exception as e:
        logMessage = f"Error moving {os.path.basename(src)}: {e}"

    with open(logFile, "a") as log:
        log.write(f"{logMessage}      [{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}]\n")

    print(logMessage)



def sortFiles(inputPath, outputPath, extensionMap, logFile):

    createOutputDirectory(outputPath)

    for root, _, files in os.walk(inputPath):

        for fileName in files:

            if not fileName.startswith("."):
                fileExtension = os.path.splitext(fileName)[1].lower()
                moved = False

                for category, extensions in extensionMap.items():

                    if fileExtension in extensions:
                        categoryPath = os.path.join(outputPath, category)

                        createOutputDirectory(categoryPath)
                        moveFile(os.path.join(root, fileName), os.path.join(categoryPath, fileName), logFile)

                        moved = True

                        break

                if not moved:
                    unsortedPath = os.path.join(outputPath, "unsorted")
                    createOutputDirectory(unsortedPath)
                    moveFile(os.path.join(root, fileName), os.path.join(unsortedPath, fileName), logFile)



def main():
    parser = argparse.ArgumentParser(description="Sort files in a directory based on their extensions.")
    parser.add_argument("-c", "--config", type=str, default="config.json", help="Path to the configuration file.")
    args = parser.parse_args()

    inputPath = getInputDirectory()
    outputPath = "output"
    randStr = "".join(random.choices("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789", k=6))
    logFile = f"log{randStr}.txt"

    config = loadConfig(args.config)
    sortFiles(inputPath, outputPath, config, logFile)



if __name__ == "__main__":
    main()

    input("Program was executed successfuly...")
