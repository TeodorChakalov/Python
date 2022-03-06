username = input()
password = input()

current_password = ""

while password != current_password:
    current_password = input()

if current_password == password:
    print(f"Welcome {username}!")