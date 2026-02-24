def two_sum(numbers, target):
    num_array = {}
    for i in range(len(numbers)):
        if target - numbers[i] in num_array:
            return [num_array[target - numbers[i]], i]
        num_array[numbers[i]] = i
    return []

array_length = int(input("Enter the number of elements in the array: "))
if array_length < 2:
    print("Array must have at least two elements.")
    exit()
else:
    numbers = []
    for i in range(array_length):
        num = int(input(f"Enter element {i + 1}: "))
        numbers.append(num)

    target = int(input("Enter the target sum: "))
    result = two_sum(numbers, target)
    print("Indices of the two numbers:", result)