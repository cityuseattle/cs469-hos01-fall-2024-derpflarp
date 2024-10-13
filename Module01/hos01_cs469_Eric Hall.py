def binarySearch(arr, target):
    # initialize the lower bound and upper bound
    low, high = 0, len(arr) - 1
    while low <= high:
        # check middle ele
        mid = (low + high) // 2
        guess = arr[mid]
        # found target
        if guess == target:
            return mid
        # guess too high
        if guess > target:
            high = mid - 1
        # guess too low
        else:
            low = mid + 1
    # target doesn't exist
    return None

# test case 1
input = [1, 3, 5, 9, 10, 11]
target = 3
print(binarySearch(input, target)) # 1

# test case 2
input = ["apple", "banana", "cherries", "grapes", "orange"]
target = "grapes"
print(binarySearch(input, target)) # 2