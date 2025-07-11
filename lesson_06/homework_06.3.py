lst1 = ['1', '2', 3, True, 'False', 5, '6', 7, 8, 'Python', 9, 0, 'Lorem Ipsum']
list2 = []
for item in lst1:
    if isinstance(item, str):
        list2.append(item)

#Альтернативне рішення
#list2 = list(filter(lambda x: isinstance(x, str), lst1))

print(list2)
