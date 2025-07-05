from itertools import count
from operator import index

adwentures_of_tom_sawer = """\
Tom gave up the brush with reluctance in his .... face but alacrity
in his heart. And while
the late steamer
"Big Missouri" worked ....
and sweated
in the sun,
the retired artist sat on a barrel in the .... shade close by, dangled his legs,
munched his apple, and planned the slaughter of more innocents.
There was no lack of material;
boys happened along every little while;
they came to jeer, but .... remained to whitewash. ....
By the time Ben was fagged out, Tom had traded the next chance to Billy Fisher for
a kite, in good repair;
and when he played
out, Johnny Miller bought
in for a dead rat and a string to swing it with—and so on, and so on,
hour after hour. And when the middle of the afternoon came, from being a
poor poverty, stricken boy in the .... morning, Tom was literally
rolling in wealth."""

##  ПЕРЕЗАПИСУЙТЕ зміст змінної adwentures_of_tom_sawer у завданнях 1-3
# task 01 ==
""" Дані у строці adwentures_of_tom_sawer розбиті випадковим чином, через помилку.
треба замінити кінець абзацу на пробіл .replace("\n", " ")"""

adwentures_of_tom_sawer = """\
Tom gave up the brush with reluctance in his .... face but alacrity
in his heart. And while
the late steamer
"Big Missouri" worked ....
and sweated
in the sun,
the retired artist sat on a barrel in the .... shade close by, dangled his legs,
munched his apple, and planned the slaughter of more innocents.
There was no lack of material;
boys happened along every little while;
they came to jeer, but .... remained to whitewash. ....
By the time Ben was fagged out, Tom had traded the next chance to Billy Fisher for
a kite, in good repair;
and when he played
out, Johnny Miller bought
in for a dead rat and a string to swing it with—and so on, and so on,
hour after hour. And when the middle of the afternoon came, from being a
poor poverty, stricken boy in the .... morning, Tom was literally
rolling in wealth."""
print(adwentures_of_tom_sawer.replace("\n", " "))

# task 02 ==
""" Замініть .... на пробіл
"""
adwentures_of_tom_sawer = """Tom gave up the brush with reluctance in his .... face but alacrity in his heart. And while the late steamer "Big Missouri" worked .... and sweated in the sun, the retired artist sat on a barrel in the .... shade close by, dangled his legs, munched his apple, and planned the slaughter of more innocents. There was no lack of material; boys happened along every little while; they came to jeer, but .... remained to whitewash. .... By the time Ben was fagged out, Tom had traded the next chance to Billy Fisher for a kite, in good repair; and when he played out, Johnny Miller bought in for a dead rat and a string to swing it with—and so on, and so on, hour after hour. And when the middle of the afternoon came, from being a poor poverty, stricken boy in the .... morning, Tom was literally rolling in wealth."""

print(adwentures_of_tom_sawer.replace("....", " "))
# task 03 ==
""" Зробіть так, щоб у тексті було не більше одного пробілу між словами.
"""
adwentures_of_tom_sawer = """Tom gave up the brush with reluctance in his   face but alacrity in his heart. And while the late steamer "Big Missouri" worked   and sweated in the sun, the retired artist sat on a barrel in the   shade close by, dangled his legs, munched his apple, and planned the slaughter of more innocents. There was no lack of material; boys happened along every little while; they came to jeer, but   remained to whitewash.   By the time Ben was fagged out, Tom had traded the next chance to Billy Fisher for a kite, in good repair; and when he played out, Johnny Miller bought in for a dead rat and a string to swing it with—and so on, and so on, hour after hour. And when the middle of the afternoon came, from being a poor poverty, stricken boy in the   morning, Tom was literally rolling in wealth. """
print(adwentures_of_tom_sawer.replace("   ", " "))

# task 04
""" Виведіть, скількі разів у тексті зустрічається літера "h"
"""
adwentures_of_tom_sawer = adwentures_of_tom_sawer.count("h")
print(f"There is {adwentures_of_tom_sawer} h in sentences.")

# task 05
""" Виведіть, скільки слів у тексті починається з Великої літери?
"""
adwentures_of_tom_sawer = """Tom gave up the brush with reluctance in his face but alacrity in his heart. And while the late steamer "Big Missouri" worked and sweated in the sun, the retired artist sat on a barrel in the shade close by, dangled his legs, munched his apple, and planned the slaughter of more innocents. There was no lack of material; boys happened along every little while; they came to jeer, but remained to whitewash. By the time Ben was fagged out, Tom had traded the next chance to Billy Fisher for a kite, in good repair; and when he played out, Johnny Miller bought in for a dead rat and a string to swing it with—and so on, and so on, hour after hour. And when the middle of the afternoon came, from being a poor poverty, stricken boy in the morning, Tom was literally rolling in wealth."""
word = 'A'
counter = 0
for word in adwentures_of_tom_sawer:
    if word.isupper():
        counter += 1
print(f"There is {counter} words in sentenсes")

# task 06
""" Виведіть позицію, на якій слово Tom зустрічається вдруге
"""
adwentures_of_tom_sawer = """Tom gave up the brush with reluctance in his face but alacrity in his heart. And while the late steamer "Big Missouri" worked and sweated in the sun, the retired artist sat on a barrel in the shade close by, dangled his legs, munched his apple, and planned the slaughter of more innocents. There was no lack of material; boys happened along every little while; they came to jeer, but remained to whitewash. By the time Ben was fagged out, Tom had traded the next chance to Billy Fisher for a kite, in good repair; and when he played out, Johnny Miller bought in for a dead rat and a string to swing it with—and so on, and so on, hour after hour. And when the middle of the afternoon came, from being a poor poverty, stricken boy in the morning, Tom was literally rolling in wealth."""
print(adwentures_of_tom_sawer.find("Tom", 1))

# task 07
""" Розділіть змінну adwentures_of_tom_sawer по кінцю речення.
Збережіть результат у змінній adwentures_of_tom_sawer_sentences
"""
adventures_of_tom_sawer_sentences = None
adwentures_of_tom_sawer = """Tom gave up the brush with reluctance in his face but alacrity in his heart. And while the late steamer "Big Missouri" worked and sweated in the sun, the retired artist sat on a barrel in the shade close by, dangled his legs, munched his apple, and planned the slaughter of more innocents. There was no lack of material; boys happened along every little while; they came to jeer, but remained to whitewash. By the time Ben was fagged out, Tom had traded the next chance to Billy Fisher for a kite, in good repair; and when he played out, Johnny Miller bought in for a dead rat and a string to swing it with—and so on, and so on, hour after hour. And when the middle of the afternoon came, from being a poor poverty, stricken boy in the morning, Tom was literally rolling in wealth"""
adwentures_of_tom_sawer_sentences = adwentures_of_tom_sawer.split(".")
for sentence in adwentures_of_tom_sawer_sentences:
    if sentence.strip():
        print(sentence.strip() + ".")


# task 08
""" Виведіть четверте речення з adwentures_of_tom_sawer_sentences.
Перетворіть рядок у нижній регістр.
"""
print(f"Sentence:\n{adwentures_of_tom_sawer_sentences[3]}")
print(f"Lower register:\n{adwentures_of_tom_sawer_sentences[3].lower()}")

# task 09
""" Перевірте чи починається якесь речення з "By the time".
"""
words = "By the time"
for i, sentence in enumerate (adwentures_of_tom_sawer_sentences):
    if words in sentence:
        print(f"The sentence begins with ‘By the time’:\n{sentence}\n")
# task 10
""" Виведіть кількість слів останнього речення з adwentures_of_tom_sawer_sentences.
"""
last_sentence = adwentures_of_tom_sawer_sentences[-2]
last_sentence = last_sentence.strip()
words_quantity = last_sentence.split(" ")
print(f'The number of words in the last sentence: {len(words_quantity)}')