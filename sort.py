def sortList(numList):
    size = len(numList)

    for i in range(size):
        for j in range(0, size - i - 1):
            if (numList[j] < numList[j + 1]):
                temp = numList[j]
                numList[j] = numList[j + 1]
                numList[j + 1] = temp

def printIntArray(arr):
    for i in range(len(arr)):
        print ("%d" %arr[i], end=" ")

def main():
    print("Please input 10 integers")
    numList = [];
    for x in range(10):
        newNum = input("> ")
        numList.append(int(newNum))
    print("\n\nUnsorted List: ", end="")
    printIntArray(numList)
    sortList(numList)
    print ("\n\nSorted List: ", end="")
    printIntArray(numList)

main()