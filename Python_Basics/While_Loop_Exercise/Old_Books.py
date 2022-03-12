book = input()
current_book = ""
sum = 0

while current_book != book:
    current_book = input()
    if current_book == book:
        print(f"You checked {sum} books and found it.")
        break
    if current_book == "No More Books":
        break
    sum += 1

if current_book == "No More Books":
    print("The book you search is not here!")
    print(f"You checked {sum} books.")