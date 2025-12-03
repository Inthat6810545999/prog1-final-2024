# Name: Inthat # Student ID: 68010545999

while True:
    sentance = input("Enter a sentence (or 'exit' to quit): ").lower()
    if sentance == "exit":
        print("Goodbye!")
        break
    vowels = 'aeiou'
    count = 0

    for i in sentance:
        if i in vowels:
            count += 1

    print(f"Vowels: {count:.0f}")