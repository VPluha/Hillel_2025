alice_in_wonderland = ("Would you tell me, please, which way I ought to go from here?\n"
                      "That depends a good deal on where you want to get to, said the Cat.\n"
                      "I don\'t much care where —— said Alice.\n"
                      "Then it doesn\'t matter which way you go, said the Cat.\n"
                      "—— so long as I get somewhere, Alice added as an explanation.\n"
                      "Oh, you\'re sure to do that, said the Cat, if you only walk long enough.\n")
print(alice_in_wonderland)
# task 01 == Розділіть змінну alice_in_wonderland так, щоб вона займала декілька фізичних лінії
# task 02 == Знайдіть та відобразіть всі символи одинарної лапки (') у тексті
# task 03 == Виведіть змінну alice_in_wonderland на друк


"""
    # Задачі 04 -10:
    # Переведіть задачі з книги "Математика, 5 клас"
    # на мову пітон і виведіть відповідь, так, щоб було
    # зрозуміло дитині, що навчається в п'ятому класі
"""
# task 04
"""
Площа Чорного моря становить 436 402 км2, а площа Азовського
моря становить 37 800 км2. Яку площу займають Чорне та Азов-
ське моря разом?
"""
black_sea = 436402
azov_sea = 37800
black_azov = black_sea + azov_sea
print(black_azov)

# task 05
"""
Мережа супермаркетів має 3 склади, де всього розміщено
375 291 товар. На першому та другому складах перебуває
250 449 товарів. На другому та третьому – 222 950 товарів.
Знайдіть кількість товарів, що розміщені на кожному складі.
"""
Total = 375291
First_Second_Storage = 250449
Second_Third_Storage = 222950
First_Storage = Total - Second_Third_Storage
Third_Storage = Total - First_Second_Storage
Second_Storage = Total - (First_Storage + Third_Storage)
print(First_Storage)
print(Second_Storage)
print(Third_Storage)

# task 06
"""
Михайло разом з батьками вирішили купити комп’ютер, ско-
риставшись послугою «Оплата частинами». Відомо, що сплачу-
вати необхідно буде півтора року по 1179 грн/місяць. Обчисліть
вартість комп’ютера.
"""
Credit_Time = 18
Payment = 1179
PC_Cost = 1179 * 18
print(PC_Cost)

# task 07
"""
Знайди остачу від діленя чисел:
a) 8019 : 8     d) 7248 : 6
b) 9907 : 9     e) 7128 : 5
c) 2789 : 5     f) 19224 : 9
"""
a = 8019 % 8
b = 9907 % 9
c = 2789 % 5
d = 7248 % 6
e = 7128 % 5
f = 19224 % 9
print(a)
print(b)
print(c)
print(d)
print(e)
print(f)

# task 08
"""
Іринка, готуючись до свого дня народження, склала список того,
що їй потрібно замовити. Обчисліть, скільки грошей знадобиться
для даного її замовлення.
Назва товару    Кількість   Ціна
Піца велика     4           274 грн
Піца середня    2           218 грн
Сік             4           35 грн
Торт            1           350 грн
Вода            3           21 грн
"""
big_pizza_cost = 274 * 4
small_pizza_cost = 218 * 2
Juice_cost = 35 * 4
Cake_cost = 350 * 1
water_cost = 21 * 3
print(big_pizza_cost + small_pizza_cost + Juice_cost + Cake_cost + water_cost)
# task 09
"""
Ігор займається фотографією. Він вирішив зібрати всі свої 232
фотографії та вклеїти в альбом. На одній сторінці може бути
розміщено щонайбільше 8 фото. Скільки сторінок знадобиться
Ігорю, щоб вклеїти всі фото?
"""
photos = 232
first_page = 8
all_pages = photos / first_page
print(all_pages)
# task 10
"""
Родина зібралася в автомобільну подорож із Харкова в Буда-
пешт. Відстань між цими містами становить 1600 км. Відомо,
що на кожні 100 км необхідно 9 літрів бензину. Місткість баку
становить 48 літрів.
1) Скільки літрів бензину знадобиться для такої подорожі?
2) Скільки щонайменше разів родині необхідно заїхати на зап-
равку під час цієї подорожі, кожного разу заправляючи пов-
ний бак?
"""
distance_1 = 1600
distance_2 = 100
fuel_usage = 9
tank_capacity = 48
fuel_needed_1 = distance_1 / distance_2
fuel_needed_2 = fuel_needed_1 * fuel_usage
pitstop = fuel_needed_2 / tank_capacity
print(fuel_needed_2)
print(pitstop)