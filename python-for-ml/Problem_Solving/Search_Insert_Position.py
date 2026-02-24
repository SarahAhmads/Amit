def search_insert(nums, target):
    left, right = 0, len(nums) - 1

    while left <= right:
        mid = left + (right - left) // 2

        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return left

num_array = int(input("Enter the number of elements in the array: "))
if num_array <= 1:
    print("Array must have at least two elements.")
    exit()
else:
    nums = []
    for i in range(num_array):
        element = int(input(f"Enter element {i + 1}: "))
        nums.append(element)
    nums.sort()
    target = int(input("Enter the target value: "))
    index = search_insert(nums, target)
    print("Index of the target value:", index)