arr = [1, 2, 5, 9, 12, 4, 6, 7, 16, 3]

def InserionSort():
    for bluep in range(1, len(arr)):
        for blackp in range(0, bluep):
            if arr[bluep] < arr[blackp]:
                temp = arr[bluep]
                for revp in range(bluep, blackp, -1):
                    arr[revp] = arr[revp -1]
                arr[blackp] = temp
                break


#a simple simple can be like
print('array before sorting', arr)
InserionSort()
print('array after sorting', arr)
