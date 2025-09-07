
def filter_even_numbers(numbers):
    even_numbers = []
    for n in numbers:
        if n % 2 == 0:
            even_numbers.append(n)
    return even_numbers


nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
filtered = filter_even_numbers(nums)

print("Original list:", nums)
print("List with even numbers only:", filtered)