# The below function reverses a string that the user inputs by using that input as a parameter.
def reverseString(inputStr):
    #Ignores case so that the string can be checked properly.
    inputStr = inputStr.lower()
    return inputStr[::-1]

# The function below executes the code of the entire application.
def main():
    userInput = input("Enter the string you would like to reverse: ")
    reversedStr = reverseString(userInput)
    print(f"Reversed string: {reversedStr}")

# Runs the main function which executes the code in the application.
if __name__ == "__main__":
    main()
