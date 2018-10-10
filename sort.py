def sortList(numbers):
    size = len(numbers)

    for i in range(size):
        for j in range(0, size - i - 1):
            if (numbers[j] < numbers[j + 1]):
                temp = numbers[j]
                numbers[j] = numbers[j + 1]
                numbers[j + 1] = temp

def printIntArray(arr):
    for i in range(len(arr)):
        print ("%d" %arr[i], end=" ")

def main():
    print("Please input 10 integers")
    numbers = [];
    for x in range(10):
        newNumber = input("> ")
        numbers.append(int(newNumber))
    print("\n\nUnsorted List: ", end="")
    printIntArray(numbers)

    sortList(numbers)
    print ("\n\nSorted List: ", end="")
    printIntArray(numbers)

main()