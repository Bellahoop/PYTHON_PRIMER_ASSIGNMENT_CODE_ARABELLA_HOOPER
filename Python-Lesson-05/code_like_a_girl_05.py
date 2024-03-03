program_purpose = input("This program checks whether a word or sentence is a palindrome. Would you like to proceed? (yes/no): ")
if program_purpose.lower() != 'yes':
    print("Please run this program again if you want to check whether a word or sentence is a palindrome.")
else:
    while True:
        palindrome_input = input("Please enter the word or sentence you would like to check: ")
        cleaned_input = ''.join(char.lower() for char in palindrome_input if char.isalpha())
        
        if not cleaned_input:
            print("Error: Please enter a word or sentence containing at least one letter.")
        else:
            input_list = list(cleaned_input)
            if cleaned_input == cleaned_input[::-1]:
                print(f"'{palindrome_input}' is a palindrome.")
            else:
                print(f"'{palindrome_input}' is not a palindrome.")
    
            print("Characters in the input:".ljust(25), input_list)
            
            print("Reversed characters:".ljust(25), input_list[::-1])
        
        another_check = input("Do you want to check another word or sentence? (yes/no): ")
        if another_check.lower() != 'yes':
            print("Please run the program again if you want to check whether a word or sentence is a palindrome.") 
            break
