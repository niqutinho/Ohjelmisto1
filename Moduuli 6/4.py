def sum_of_list(numbers):
    total = 0
    for n in numbers:
        total += n
    return total


nums = [3, 7, 2, 8, 5]
result = sum_of_list(nums)
print(f"The sum of the numbers in the list is: {result}")

