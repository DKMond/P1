print("Exercitiul 1")

for V1 in range(11):
    print(V1)
# ____________________________________________________________________________
print("Exercitiul 2")

print('Te rugam introduce emailul si parola pentru a continua')
EMAIL_ADRESS = input('Adresa de email: ')
EMAIL_PASSWORD = input('Parola: ')

if EMAIL_ADRESS == 'george21@foxgg.com' and EMAIL_PASSWORD == 'Ceva2123':
    print("Bun Venit George")
else:
    print('Emailul sau parola sunt incorecte')
# _____________________________________________________________________________
print("Exercitiul 3")
V3 = input()
if len(V3) == 10:
    print("numarul este valid")
elif len(V3) < 10:
    print("numarul este invalid")
elif len(V3) > 10:
    print("numarul este invalid:")
# _______________________________________________________________________________
print("Exercitiul 4")
print("Verificator de cnp-uri")
CNP = input()

if len(CNP) == 13:
    CNP = True
elif len(CNP) < 13:
    CNP = False
elif len(CNP) > 13:
    CNP = False
if CNP is True:
    print('CNP-ul este valid')
elif CNP is False:
    print('CNP-ul este invalid')
# Nu mai am ideii
