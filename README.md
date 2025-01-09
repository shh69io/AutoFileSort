# AutoFileSort

AutoFileSort is a simple yet powerful Python tool designed to help you declutter your directories by automatically organizing files based on their extensions. Whether you're a student, a professional, or just someone looking to keep your files tidy, AutoFileSort has you covered!

---

## Features
- **Automatic File Sorting**: Categorizes files into predefined folders like `Documents`, `Images`, `Audio`, `Video`, etc.
- **Customizable Configurations**: Supports custom `config.json` files for better control over file categorization.
- **Enhanced Logging**: Logs now include timestamps and detailed summaries of file movements.
- **Improved Error Handling**: Provides better error feedback if a file move operation fails, including specific error messages.
- **File Permissions Check**: Checks file permissions before attempting to move them, ensuring there are no issues with read/write access.
- **Optional Directory Structure Preservation**: Keep the original directory structure while organizing files into categories.
- **Log Header**: A header is added to each log file to track the start date/time and the overall sorting process.
- **File Type Summary**: A summary of how many files of each type were moved is displayed at the end and included in the log file.
  
---

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/AutoFileSort.git
   ```
2. Ensure [Python 3.5+](https://www.python.org/downloads/) is installed on your system. No external libraries required!

---

## Usage
1. Run the program:
   ```bash
   python AutoFileSort.py
   ```

   For using custom `config.json` files:
   ```bash
   python AutoFileSort.py -c config.json
   ```
2. Enter the path to the directory you wish to organize when prompted.
3. Files will be sorted into an `output` folder, categorized into subfolders based on their type.
4. Check the generated log file for a summary of all file movements.

---

## How It Works
1. **Input Validation**: Ensures the provided directory exists and can be accessed.
2. **File Categorization**: Matches file extensions to categories defined in `config.json` or follows the default configuration.
3. **Output Structure**: Creates categorized folders dynamically within the `output` directory.
4. **Logging and Feedback**: Logs each file movement and provides real-time updates in the terminal.
5. **Permission and Error Handling**: Ensures that files can be accessed and moved, with error details logged if issues arise.

---

## Example
### Input Directory:
```
/path/to/input/directory/
```
### Output Directory:
```
output/
    documents/
        report.pdf
    images/
        photo.jpg
    audio/
        song.mp3
    unsorted/
        unknown_file.xyz
```

---

## What's New in v1.2
- **Improved Logging**: Log files now include a header with the start date/time and detailed summaries of each file movement.
- **File Permissions Check**: Ensures files can be read/written before moving them, preventing access errors.
- **Directory Structure Preservation**: Optionally preserve the directory structure when sorting files into categories.
- **File Type Summary**: Display a summary of the number of files sorted into each category, included in the log.
- **Error Handling Improvements**: Provide more informative error messages during file operations.

---

## License
AutoFileSort is open-source and available under the [MIT License](LICENSE.txt).
