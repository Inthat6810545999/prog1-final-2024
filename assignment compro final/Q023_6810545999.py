# Name: Inthat # Student ID: 68010545999

rd = open("journal.log" , "a")

while True:
    journal = input("Enter journal entry (or 'DONE' to exit): ")
    if journal == "DONE":
        print("Journal closed.")
        break

    rd.write(journal + "\n")
    print("Entry saved.")

rd.close()
