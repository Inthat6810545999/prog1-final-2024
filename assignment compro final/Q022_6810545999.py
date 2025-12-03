# Name: Inthat # Student ID: 68010545999

from pathlib import Path

filename = input("Enter the filename to read: ")

filename_path = Path(filename)



if filename_path.exists():
    f = open(f"{filename}", "r")
    print("--- File Content ---")
    content = f.read()
    print(content)
    print("")
    print("--- Word Count ---")
    count = len(content.split())
    print(f"Total words: {count}")

else:
    print(f"Error: The file '{filename}' was not found.")