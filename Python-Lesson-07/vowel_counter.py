def vowel_counting(name):
    vowels = "AEIOUaeiou"
    count = 0
    for char in name:
        if char in vowels:
            count += 1
    print(f"The name is {name}.")
    print(f"And it has {count} vowels.")
    
def main():
    print("This program counts the number of vowels in a name.")

    while True:
        name = input("\nEnter the name (or type 'exit' to quit): ")

        if name.lower() == 'exit':
            print("Exiting the program. Thank you!")
            break

        if name.replace(" ", "").isalpha():
            vowel_counting(name)
        else:
            print("Please enter the name containing only alphabetic characters and spaces.")

        while True:
            another_name = input("\nWould you like to check another name? (yes/no): ").lower()
            if another_name in ['yes', 'no']:
                break
            else:
                print("Invalid input. Please enter 'yes' or 'no'.")

        if another_name == 'no':
            print("Exiting the program. Thank you!")
            break

if __name__ == "__main__":
        main()
        
