# Method to sort an array of integers using Bubble sort
def sortList(numbers):
    size = len(numbers)

    for i in range(size):
        for j in range(0, size - i - 1):
            if (numbers[j] < numbers[j + 1]):
                temp = numbers[j]
                numbers[j] = numbers[j + 1]
                numbers[j + 1] = temp

# Method to print the array of integers on one line
def printIntArray(arr):
    for i in range(len(arr)):
        print ("%d" %arr[i], end=" ")

def main():
    # Get 10 integers from the user and append them to an array
    print("Please input 10 integers")
    numbers = [];
    for x in range(10):
        newNumber = input("> ")
        numbers.append(int(newNumber))

    # Print the array as it was inputted
    print("\n\nUnsorted List: ", end="")
    printIntArray(numbers)

    # Sort the array and print it in sorted order
    sortList(numbers)
    print ("\n\nSorted List: ", end="")
    printIntArray(numbers)

main()