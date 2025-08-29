Overview

This Python program demonstrates file handling with error handling.
It asks the user for a filename, reads its content, modifies the text (by default converting it to uppercase), and writes the modified version to a new file.

The program gracefully handles common errors such as:

File not found ❌

Permission denied 🚫

Unexpected runtime errors ⚠️

⚙️ Features

✅ Reads content from an existing file

✅ Applies modifications to the text (uppercase conversion by default)

✅ Saves modified content into a new file (modified_<filename>)

✅ Handles errors safely with clear messages

How to Run

Clone or download the project files.

Open a terminal in the project directory.

Run the program:

python main.py

Enter the name of the file you want to read when prompted.

📝 Example Usage
Input File (notes.txt):
Python is fun!
Error handling is important.

Program Run:
Enter the name of the file to read: notes.txt
✅ File modified and saved as 'modified_notes.txt'

Output File (modified_notes.txt):
PYTHON IS FUN!
ERROR HANDLING IS IMPORTANT.

🛠 Requirements

Python 3.6+
