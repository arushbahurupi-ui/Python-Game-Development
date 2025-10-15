dictionary = {}

print("  ")
print("--- Dictionary ---")
print("  ")
print("1 = View")
print("2 = Add")
print("3 = Remove")
print("4 = Change")
print("5 = Exit")
print("   ")

while True:
    choice = input("Enter your choice: ")
    if choice == "1":
        for i,j in dictionary.items():
            print(i + " - " + j)
    elif choice == "2":
        key = input("Enter key: ")
        value = input("Enter value: ")
        dictionary[key] = value
    elif choice == "3":
        key = input("Enter key: ")
        if key in dictionary.keys():
            del dictionary[key]
        else:
            print("Key not found")
    elif choice == "4":
        key = input("Enter key: ")
        if key in dictionary.keys():
            value = input("Enter value: ")
            dictionary[key] = value
        else:
            print("Key not found")

    elif choice == "5":
        break