chars = input()
unique_chars = set(chars)
print(len(unique_chars))
if unique_chars.__len__() > 10:
    print(True)
else:
    print(False)
# Підказака від колеги:
# chars = input()
# unique_chars = set(chars)
# print(len(unique_chars))
# print(unique_chars.__len__() > 10)
