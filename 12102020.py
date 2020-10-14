# print(2 > 3)
# a = None
# if 2 > 3:
#     a = True
# else:
#     a = False
#     print(a)

# a = False
# b = True
# if a is False:
#     print(a)

# a = input("Testam chestii :P")
# b = True
# if a.isdigit()  and int(a) < 100:
#     b = False
# elif a.isdigit():
#     b = True
#     print(b)

# nr1 = input("Introdu nr1: ")
# nr2 = input("Introdu nr2: ")
# a = None
#
# if int(nr1) > int(nr2):
#     a = nr1
# else:
#     a = nr2
#     print(a)

# nr1 = input("nr1: ")
# nr2 = input("nr2: ")
# if int(nr1) > int(nr2):a = nr1
# else:

nr1 = input("nr1: ")
nr2 = input("nr2: ")
nr3 = input("nr3: ")
if nr1.isdigit() and nr2.isdigit() and nr3.isdigit():
    print(max(nr1 , nr2 ,nr3))
else:
    print("nr este valid")
