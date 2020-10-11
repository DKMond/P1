print("Exercitiul 1")
V1 = [1,2,3,4,5,6,7,8,9,10]
for EachNumber in V1:
    print(EachNumber)
#__________________________________________________________________
print("Exercitiul 2")

EMAIL_ADDRESS = "george2020@ggfo.com"
EMAIL_PASSWORD = "12345678"


V2 = "12345678"
E1 = "george2020@ggfo.com"
if len(EMAIL_PASSWORD) == len(V2) and EMAIL_PASSWORD == V2:
    EMAIL_PASSWORD = True
if len(EMAIL_ADDRESS) == len(E1)\
        and EMAIL_ADDRESS == E1:
     EMAIL_ADDRESS = True

if EMAIL_ADDRESS and EMAIL_PASSWORD is True:
    print("Permisiune acordata")
else:
    print("Emailul sau parola sunt incorecte")
#__________________________________________________________________
print("Exercitiul 3")
V3 = "0767421824"
if len(V3) == 10:print("numarul este valid")
elif len(V3) < 10:print("numarul este invalid")
elif len(V3) > 10:print("numarul este invalid:")
#__________________________________________________________________
