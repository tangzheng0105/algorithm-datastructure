def findSmallest(arr):
    smallest = arr[0]
    smallest_index = 0
    for i,val in enumerate(arr):
        if(val < smallest):
            smallest = val
            smallest_index = i

    return (smallest_index,smallest)

def selectionSort(arr):
    newArr = []
    for i in range(0,len(arr)):
        smallest_index = findSmallest(arr)[0]
        newArr.append(arr.pop(smallest_index))
        print(arr)
    return newArr

if __name__ == "__main__":
    arr = [3,8,2,75,34,67,24,56,30,98,47]
    print(selectionSort(arr))