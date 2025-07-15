numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = 0
for num in numbers:
    if num % 2 == 0:
        even_numbers += num

        print(even_numbers)

# Алтернативне рішення
# even_numbers = sum(num for num in numbers if num % 2 == 0)
# print(even_numbers)