ukoly = []


def hlavni_menu():
    while True:
        print("Správce úkolů - Hlavní menu")
        print("1. Přidat nový úkol")
        print("2. Zobrazit všechny úkoly")
        print("3. Odstranit úkol")
        print("4. Konec programu")

        volba = input("Vyberte možnost (1-4): ")

        if volba in ("1", "2", "3", "4"):
            return volba

        print("Neplatná volba, zkuste to znovu.")


def pridat_ukol():
    ukol = input("Zadejte název úkolu: ")
    if ukol == "":
        print("Název úkolu nesmí být prázdný.")
        return

    ukoly.append(ukol)
    print("Úkol byl přidán.")


def zobrazit_ukoly():
    if not ukoly:
        print("Seznam úkolů je prázdný.")
        return

    for i, ukol in enumerate(ukoly, start=1):
        print(f"{i}. {ukol}")


def odstranit_ukol():
    if not ukoly:
        print("Seznam úkolů je prázdný.")
        return

    zobrazit_ukoly()
    cislo = input("Zadejte číslo úkolu k odstranění: ")

    if not cislo.isdigit():
        print("Musíte zadat číslo.")
        return

    index = int(cislo) - 1
    if index < 0 or index >= len(ukoly):
        print("Takový úkol neexistuje.")
        return

    ukoly.pop(index)
    print("Úkol byl odstraněn.")


