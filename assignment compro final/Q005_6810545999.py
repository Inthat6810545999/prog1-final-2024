# Name: Inthat # Student ID: 68010545999

text_input = input("Enter a string: ").lower()

if text_input.strip() == "":
    print("Empty input")
else:
    char_count = {}

    for ch in text_input:
        if ch != " ":
            if ch not in char_count:
                char_count[ch] = 1
            else:
                char_count[ch] += 1

    for ch in char_count:
        print(f"{ch}: {char_count[ch]}")
