arabella_dictionary = {
    "first name": "Arabella",
    "last name": "Hooper",
    "occupation": "Racecar driver",
    "hobbies": "Swimming",
    "language": "English",
    "location": "Melbourne",
}

natural_english_sentence = (
    f"My name is {arabella_dictionary['first name']} {arabella_dictionary['last name']}, "
    f"I live in {arabella_dictionary['location']}, "
    f"I work as a {arabella_dictionary['occupation']}, "
    f"I love {arabella_dictionary['hobbies']}, "
    f"I speak {arabella_dictionary['language']}."
)

def print_dictionary(dictionary):
    print("\n---Current Dictionary:---\n")
    for key, value in dictionary.items():
        print(f"My {key} is {value}.")

print_dictionary(arabella_dictionary)

while True:
    action = input("\nWhat would you like to do to the dictionary? (add, remove, update, clear, exit): ").strip().lower()

    if action == 'add':
        key = input("Enter the key you want to add: ")
        value = input("Enter the value: ")
        arabella_dictionary[key] = value
        print(f"\nAdded {key} to the dictionary.")

    elif action == 'remove':
        key = input("Enter the key you want to remove: ")
        if key in arabella_dictionary:
            del arabella_dictionary[key]
            print(f"\nRemoved {key} from the dictionary.")
        else:
            print("\nKey not found.")

    elif action == 'update':
        key = input("Enter the key you want to update: ")
        if key in arabella_dictionary:
            value = input("Enter the new value: ")
            arabella_dictionary[key] = value
            print(f"\nUpdated {key} in the dictionary.")
        else:
            print("\nKey not found.")

    elif action == 'clear':
        arabella_dictionary.clear()
        print("\nCleared the dictionary.")

    elif action == 'exit':
        print("\nExited the application. Thank you!")
        break

    else:
        print("\nInvalid action.")

    print_dictionary(arabella_dictionary)
