from task_manager_part1 import hlavni_menu, pridat_ukol, zobrazit_ukoly, odstranit_ukol


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
