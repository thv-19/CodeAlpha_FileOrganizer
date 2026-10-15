# File Organizer

## Project Overview

The File Organizer is a Python program that automatically organizes image files into a separate folder.

The program searches a specified folder for image files and moves them into an `Images` folder. This project was created as part of a Python programming internship task to practice file handling and automation in Python.

## Features

- Searches for image files automatically.
- Supports `.jpg`, `.jpeg`, `.png`, and `.gif` files.
- Creates the `Images` folder automatically if it does not exist.
- Moves image files from the source folder to the destination folder.
- Displays the files that have been moved.
- Uses Python's built-in file-handling modules.

## Technologies Used

- Python 3
- `os` module
- `shutil` module

## Python Modules

### OS

The `os` module is used to work with folders, file paths, and directory contents.

### Shutil

The `shutil` module is used to move files from one folder to another.

## How It Works

The program follows these steps:

1. Sets the source folder containing the files.
2. Sets the destination folder named `Images`.
3. Creates the `Images` folder if it does not already exist.
4. Checks the files inside the source folder.
5. Identifies image files based on their file extensions.
6. Moves the image files into the `Images` folder.
7. Displays a message showing which files were moved.

## How to Run

1. Make sure Python 3 is installed.
2. Open the project folder in VS Code.
3. Place image files inside the `TestFiles` folder.
4. Open the VS Code terminal.
5. Run:

```bash
python file_organizer.py
```
6. The program will automatically move supported image files into the `Images` folder.

## Supported File Types

The program supports the following image formats:

- `.jpg`
- `.jpeg`
- `.png`
- `.gif`

## Example

### Before running the program:

```text
TestFiles/
├── photo1.jpg
├── photo2.png
└── picture.gif

Images/
```
### After running the program
```text
TestFiles/

Images/
├── photo1.jpg
├── photo2.png
└── picture.gif
```

### Example:
```text
Images folder is ready!
Moved image: photo1.jpg
Moved image: photo2.png
Moved image: picture.gif
File organization completed!
```
## Project Purpose
This project demonstrates basic file automation in Python. It shows how Python can be used to search directories, identify files by their extensions, create folders, and move files automatically.