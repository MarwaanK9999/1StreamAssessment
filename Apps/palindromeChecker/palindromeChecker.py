# This function checks if the user has entered a palindrome.
def isPalindrome(inputString):
    #Ignores case so that a palindrome string entered with one upper case letter is seen as a palindrome.
    inputString = inputString.lower()
    return inputString == inputString[::-1]

# The function below executes the code of the entire application.
def main():
    # Take input is taken from the user.
    inputString = input("Enter a string to see if it is a palindrome: ")

    # Execute the isPalindrome function with the input as a parameter.
    result = isPalindrome(inputString)

    # End result based on the result that is given by the isPalindrome function.
    if result:
        print("Yes, it is a palindrome")
    else:
        print("No, it is not a palindrome.")

# Runs the main function which executes the code in the application.
if __name__ == "__main__":
    main()