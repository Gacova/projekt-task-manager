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
    while True:
        print()
        nazev = input("Zadejte název úkolu: ")
        popis = input("Zadejte popis úkolu: ")

        if nazev == "" or popis == "":
            continue

        ukoly.append({"nazev": nazev, "popis": popis})
        print(f"Úkol '{nazev}' byl přidán.")
        return


def zobrazit_ukoly():
    if not ukoly:
        print("Seznam úkolů je prázdný.")
        return

    print("\nSeznam úkolů:")
    for i, ukol in enumerate(ukoly, start=1):
        print(f"{i}. {ukol['nazev']} - {ukol['popis']}")


def odstranit_ukol():
    if not ukoly:
        print("Seznam úkolů je prázdný.")
        return

    print("\nSeznam úkolů:")
    for i, ukol in enumerate(ukoly, start=1):
        print(f"{i}. {ukol['nazev']} - {ukol['popis']}")

    cislo = input("\nZadejte číslo úkolu, který chcete odstranit: ")

    if not cislo.isdigit():
        print("Zadaný úkol neexistuje.")
        return

    index = int(cislo) - 1

    if index < 0 or index >= len(ukoly):
        print("Zadaný úkol neexistuje.")
        return

    odstraneny = ukoly.pop(index)
    print(f"Úkol '{odstraneny['nazev']}' byl odstraněn.")


def main():
    while True:
        volba = hlavni_menu()

        if volba == "1":
            pridat_ukol()
        elif volba == "2":
            zobrazit_ukoly()
        elif volba == "3":
            odstranit_ukol()
        elif volba == "4":
            print("Konec programu.")
            break


if __name__ == "__main__":
    main()

