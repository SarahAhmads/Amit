def reverse_add(num1, num2):
    rev_num1 = int(str(num1)[::-1])
    rev_num2 = int(str(num2)[::-1])
    
    rev_sum = rev_num1 + rev_num2
    final_result = int(str(rev_sum)[::-1])
    
    return final_result

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

result = reverse_add(num1, num2)
print("Final result:", result)