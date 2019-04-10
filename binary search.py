array = [4,7,8,3,9,213,87,41]
array = sorted(array)
print(array)
def search(item):
    left = 0
    right = len(array)-1
    while left<=right:
        mid =(left+right)//2
        if array[mid]==item:
            return mid
        elif array[mid]>item:
            right = mid-1
        elif array[mid]<item:
            left = mid+1

    return -1
print(search(9))
