import random
from words import lista_cuvinte


def afiseaza_spanzuratoarea(incercari):
    """

    :param incercari: 8
    :return: returneaza stagile incomplete ale spanzuratoearei
    """
    stagii = [
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                """,

                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                """,

                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                """,

                """
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                """,

                """
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                """,

                """
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                """,

                """
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                """
    ]
    return stagii[incercari]


def obtine_cuvant():
    cuvant = random.choice(lista_cuvinte)
    return cuvant.upper()


def joaca(cuvant):
    """

    :param cuvant: este cuvantul ce trebuie ghicit
    :return:
    """
    completarea_cuvantului = "_" * len(cuvant)
    ghicit = False
    litere_ghicite = []
    cuvinte_ghicite = []
    incercari = 6
    print("Hai sa jucam spanzuratoarea!")
    print(afiseaza_spanzuratoarea(incercari))
    print(completarea_cuvantului)
    print("\n")
    while not ghicit and incercari > 0:
        ghici = input("Te rog sa ghicesti o litera sau un cuvant: ").upper()
        if len(ghici) == 1 and ghici.isalpha():
            if ghici in litere_ghicite:
                print("deja ai ghicit aceasta litera", ghici)
            elif ghici not in cuvant:
                print(ghici, "nu este in cuvant.")
                incercari -= 1
                litere_ghicite.append(ghici)
            else:
                print(ghici + " este in cuvant")
                litere_ghicite.append(ghici)
                cuvant_ca_lista = list(completarea_cuvantului)
                indici = [i for i, litera in enumerate(cuvant) if litera == ghici]
                for index in indici:
                    cuvant_ca_lista[index] = ghici
                completarea_cuvantului = "".join(cuvant_ca_lista)
                if "_" not in completarea_cuvantului:
                    ghicit = True
        elif len(ghici) == len(cuvant) and ghici.isalpha():
            if ghici in cuvinte_ghicite:
                print("deja ai ghicit aceast cuvant", ghici)
            elif ghici != cuvant:
                print(ghici, "nu este in cuvant.")
                incercari -= 1
                cuvinte_ghicite.append(ghici)
            else:
                ghicit = True
                completarea_cuvantului = cuvant
        else:
            print("carater invalid.")
        print(afiseaza_spanzuratoarea(incercari))
        print(completarea_cuvantului)
        print("\n")
    if ghicit:
        print("Felicitari ai castigat")
    else:
        print("Ai piertdut cuvantul corect era " + cuvant + ". Poate data viitoare")


def main():
    cuvant = obtine_cuvant()
    joaca(cuvant)
    while input("Joci din nou? (D/N) ").upper() == "D":
        cuvant = obtine_cuvant()
        joaca(cuvant)


if __name__ == "__main__":
    main()
