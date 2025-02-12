def fullNameSort(namesList):
    # Sorts a list of tuples (name, surname) using bubble sort algorithm.
    n = len(namesList)
    
    # Search through all elements in the list.
    for i in range(n):
        # Last i elements are already sorted.
        for j in range(0, n-i-1):
            # First compare the first names, and if they are equal, compare the surnames.
            if (namesList[j][0] > namesList[j+1][0]) or (namesList[j][0] == namesList[j+1][0] and namesList[j][1] > namesList[j+1][1]):
                # Swap the elements if the element found is greater than the next element.
                namesList[j], namesList[j+1] = namesList[j+1], namesList[j]

    return namesList

# Function to get user input of names and surnames. Returns a list of tuples with the names.
def getUserInput():
    
    userInput = []
    print("Enter Names and Surnames (type 'exit' to stop):")
    while True:
        name = input("First name: ")
        if name.lower() == 'exit':
            break
        surname = input("Surname: ")
        userInput.append((name, surname))
    return userInput

# The function below executes the code of the entire application.
def main():
    # Get the user input.
    namesList = getUserInput()
    
    # Sort the list using the bubble sort method.
    sortedNames = fullNameSort(namesList)
    
    # Print the sorted list
    print("\nSorted names:")
    for name, surname in sortedNames:
        print(f"{name} {surname}")

# Runs the main function which executes the code in the application.
if __name__ == "__main__":
    main()