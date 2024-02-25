program_purpose = input("This program checks whether a word is a palindrome. Would you like to proceed? (yes/no): ")
if program_purpose.lower() != 'yes':
    print("Please run this program again if you want to check whether a word is a palindrome.")
else:
    while True:
        word = input("Please enter the word you would like to check: ")
        if not word.isalpha():
            print("Error: Please enter a word only containing letters.")
        else:
            word_lower = word.lower()
            reversed_word = word_lower[::-1]
            if word_lower == reversed_word:
                print(f"The word '{word}' is a palindrome.")
            else:
                print(f"The word '{word}' is not a palindrome.")
        another_word = input("Do you want to check another word? (yes/no): ")
        if another_word.lower() != 'yes':
            print("Please run the program again if you want to check whether a word is a palindrome.") 
            break
