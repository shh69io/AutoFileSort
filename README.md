# AutoFileSort

AutoFileSort is a simple yet powerful Python tool designed to help you declutter your directories by automatically organizing files based on their extensions. Whether you're a student, a professional, or just someone looking to keep your files tidy, AutoFileSort has you covered!

---

## Features
- **Automatic File Sorting**: Categorizes files into predefined folders like `Documents`, `Images`, `Audio`, `Video`, etc. 
- **Customizable Configurations**: Supports custom `config.json` files for better control over file categorization.

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

## What's New in v1.1.0
- **Exhaustive Configuration**: Introduced a comprehensive `config.json` supporting a wide range of file formats.
- **Enhanced Logging**: Logs now include timestamps and detailed file movement summaries.

---

## License
AutoFileSort is open-source and available under the [MIT License](LICENSE.txt).
