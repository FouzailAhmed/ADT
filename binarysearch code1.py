# iterative code for binary search
arr = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k'] #11 characters in this array

def BinarySearch(target):
    low = 0
    high = len(arr) -1
    while low <= high:
        mid = (low + high)//2
        if arr[mid] == target:
            return (mid)
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1
#u can play around with the display but here is a simple versiom
print(BinarySearch(input('enter a valid char from a to k')))


