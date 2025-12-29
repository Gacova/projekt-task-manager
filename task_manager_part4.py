from task_manager_part1 import hlavni_menu

ukoly = []


def pridat_ukol():
    while True:
        print()
        nazev = input("Zadejte název úkolu: ")
        popis = input("Zadejte popis úkolu: ")

        if nazev == "" or popis == "":
            continue

        ukoly.append({
            "nazev": nazev,
            "popis": popis
        })

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

    zobrazit_ukoly()
    cislo = input("Zadejte číslo úkolu k odstranění: ")

    if not cislo.isdigit():
        return

    index = int(cislo) - 1
    if index < 0 or index >= len(ukoly):
        return

    ukoly.pop(index)
    print("Úkol byl odstraněn.")


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
            print("Ukončuji program.")
            break


if __name__ == "__main__":
    main()
