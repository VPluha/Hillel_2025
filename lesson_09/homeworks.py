
"""  Написати функцію, яка обчислює суму двох чисел.
"""

def sum_two_numbers(number15, number12):
    return sum([number15, number12])
print(sum_two_numbers(15, 12))

"""  Написати функцію, яка розрахує середнє арифметичне списку чисел.
"""

def average(number_list):
    if len(number_list) == 0:
        return 0
    return sum(number_list) / len(number_list)

"""  Написати функцію, яка приймає рядок та повертає його у зворотному порядку.
"""

def revers_text(text):
    return text.lower()[::-1]
print(revers_text("Madam, Racecar, Level, Radar, Rotor, Civic"))

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