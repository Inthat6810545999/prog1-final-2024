# Name: Inthat # Student ID: 68010545999

from pathlib import Path

filename = input("Enter the input filename: ")
find_word = input("Enter the word to find: ")
replaceword = input("Enter the replacement word: ")
output_filename = input("Enter the output filename: ")

file_path = Path(filename)

if file_path.exists():
    f = open(f"{filename}" , "r" , encoding="utf-8")
    new_text = f.read().replace(find_word , replaceword)
    new_file = open(f"{output_filename}" , "w" , encoding = "utf-8")
    new_file.write(new_text)
    print(f"\nReplacement complete. Content saved to {output_filename}")
    f.close()
    new_file.close()
else:
    print(f"Error: Input file '{filename}' not found.")


