# task 1
""" Задача - надрукувати табличку множення на задане число, але
лише до максимального значення для добутку - 25.
Код майже готовий, треба знайти помилки та випраавити\доповнити.
"""
import math


def multiplication_table(number):
    # Initialize the appropriate variable
    multiplier = 1

    # Complete the while loop condition.
    while number * multiplier <= 25:
        result = number * multiplier
        # десь тут помила, а може не одна
        if  result > 25:
            # Enter the action to take if the result is greater than 25
            break
        print(str(number) + "x" + str(multiplier) + "=" + str(result))

        # Increment the appropriate variable
        multiplier += 1

multiplication_table(3)
# Should print:
# 3x1=3
# 3x2=6
# 3x3=9
# 3x4=12
# 3x5=15


# task 2
"""  Написати функцію, яка обчислює суму двох чисел.
"""

def sum_two_numbers(number15, number12):
    return sum([number15, number12])
print(sum_two_numbers(15, 12))

#Альтернатива
# def sum_two_numbers(*numbers):
#     return sum(numbers)
# print(sum_two_numbers(15, 12))

# task 3
"""  Написати функцію, яка розрахує середнє арифметичне списку чисел.
"""

def average(number_list):
    return sum(number_list) / len(number_list)
print(average([9, 6, 8, 4, 5]))

# task 4
"""  Написати функцію, яка приймає рядок та повертає його у зворотному порядку.
"""

def list_of_numbers(list):
    return sorted(list, reverse=True)
print(list_of_numbers(range(10)))

# task 5
"""  Написати функцію, яка приймає список слів та повертає найдовше слово у списку.
"""

def longest_word(words):
    longest_word = words[0]
    for word in words:
        if len(word) > len(longest_word):
            longest_word = word
    return longest_word
words = ["Kherson", "Bakhmut", "Enerhodar", "Mariupol"]
print(longest_word(words))

# task 6
"""  Написати функцію, яка приймає два рядки та повертає індекс першого входження другого рядка
у перший рядок, якщо другий рядок є підрядком першого рядка, та -1, якщо другий рядок
не є підрядком першого рядка."""
def find_substring(str1, str2):
    if str2 in str1:
        index = str1.find(str2)
        return index
    else:
        return -1

str1 = "Hello, world!"
str2 = "world"
print(find_substring(str1, str2)) # поверне 7

str1 = "The quick brown fox jumps over the lazy dog"
str2 = "cat"
print(find_substring(str1, str2)) # поверне -1

# task 7
"""
Порахувати кількість унікальних символів в строці. 
Якщо їх більше 10 - вивести в консоль True, інакше - False.
Строку отримати за допомогою функції input()
"""

def unique_chars(chars):
    return len(set(chars))
chars = input()
unique_char = set(chars)
print(unique_char.__len__() >10)

# task 8
"""
Є list з даними lst1 = ['1', '2', 3, True, 'False', 5, '6', 7, 8, 'Python', 9, 0, 'Lorem Ipsum']. 
Напишіть код, який свормує новий list (наприклад lst2), який містить лише змінні типу стрінг, які присутні в lst1. 
Данні в лісті можуть бути будь якими
"""

def filter_strings(lst):
    return list(filter(lambda x: isinstance(x, str), lst))
list1 = ['1', '2', 3, True, 'False', 5, '6', 7, 8, 'Python', 9, 0, 'Lorem Ipsum']
list2 = filter_strings(list1)
print(list2)

# task 9
"""
Ігор займається фотографією. Він вирішив зібрати всі свої 232
фотографії та вклеїти в альбом. На одній сторінці може бути
розміщено щонайбільше 8 фото. Скільки сторінок знадобиться
Ігорю, щоб вклеїти всі фото?
"""
def photo_album_size(photos):
    photos_one_page = 8
    result = math.ceil(photos / photos_one_page)
    return result

while True:
    number_of_photos = input("Enter number of photos: ")
    if number_of_photos.isdigit():  # перевіряємо, що число ціле
        photos = int(number_of_photos)
        pages_required = photo_album_size(photos)
        print(f"Vasyl will need {pages_required} pages.")
        break
    else:
        print("ERROR!!! Enter an integer: ")

# task 10
""" Є ліст з числами, порахуйте сумму усіх ПАРНИХ чисел в цьому лісті """

def sum_even_numbers(numbers):
    even_sum = 0
    for num in numbers:
        if num % 2 == 0:
            even_sum += num
            print(even_sum)

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
sum_even_numbers(numbers)

"""  Оберіть будь-які 4 таски з попередніх домашніх робіт та
перетворіть їх у 4 функції, що отримують значення та повертають результат.
Обоязково документуйте функції та дайте зрозумілі імена змінним.
"""