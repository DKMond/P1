# def mesaj():
#     print("introdu ceva anume: ")
#
#
# mesaj()

# def mesaj(numar_1, numar_2):
#     print(f"introdu ceva cum ar fi {numar_1} sau {numar_2}")


# mesaj(2, 5)
# mesaj(numar_2=3, numar_1=20)

# def suma(a, c, b=2):
#     valoare_suma = a + b + c
#     return valoare_suma
#
# print(suma(1, 2))

# def suma(a, c, b=2):
#     return a + b + c, a - b - c
#
#
# valoare_suma, valoare_dif = suma(1, 2)
# print(valoare_suma, valoare_dif)

# def suma(a: int, c: int, b: int = 2) -> (list, int):
#     return [a + b + c], a - b - c
#
#
# valoare_suma, valoare_dif = suma(10, 2)
# print(valoare_suma, valoare_dif)

# def suma(a: int, c: int, b: int = 2) -> (list, int):
#     """
#     :param a:
#     :param c:
#     :param b:
#     :return: lisata de suma, diferenta
#     """
#     return [a + b + c], a - b - c
#
#
# valoare_suma, valoare_dif = suma(10, 2)
# print(valoare_suma, valoare_dif)

# def inmultire(a: int, b: int) -> (bool, int):
#     rezultat = a * b
#     return True, rezultat
#
#
# print(inmultire(1, 2))

# def listre(a: bool, b: bool) -> bool:
#     if a is True:
#         return True
#     if b is False:
#         return False
#
#
# print(listre(True, False))

def printare(a, b):
    listare(a, b)
    return True


print(printare(True, False))