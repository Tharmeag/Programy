# przywitanie i wprowadzenie użytkowanika do programu

print("Witaj w programie obliczającym Twoje zapotrzebowanie kaloryczne!")
print("Wybierz płeć:")
plec = int(input("1 - Męszczyzna 2 - Kobieta:"))
if plec == 1:
    print("Powiedz mi jaką aktywność masz na codzień:")
    xyz = int(input("1 - Niska aktywność 2 - Średnia aktywność 3 - Wysoka aktywność:"))

#   niska aktywność
    if xyz == 1:
        x = int(input("Podaj swoją wagę:"))
        waga1 = (x * 10)
        y = int(input("Podaj swój wzrost w centymetrach:"))
        wzrost1 = (y * 6.25)
        z = int(input("Podaj swój wiek:"))
        wiek1 = (z * 5)
        wynik = int((waga1 + wzrost1 - wiek1) + 5)
        wynik1 = int(wynik * 1.2 - 500)
        print(str(wynik1) + "kcal" + " " + "Tyle kalorii potrzebujesz aby schudnąć! :)")

#   średnia aktywność
    elif xyz <= 2:
        x = int(input("Podaj swoją wagę:"))
        waga1 = (x * 10)
        y = int(input("Podaj swój wzrost w centymetrach:"))
        wzrost1 = (y * 6.25)
        z = int(input("Podaj swój wiek:"))
        wiek1 = (z * 5)
        wynik = int((waga1 + wzrost1 - wiek1) + 5)
        wynik1 = int(wynik * 1.4 - 500)
        print(str(wynik1) + "kcal" + " " + "Tyle kalorii potrzebujesz aby schudnąć! :)")

# Wysoka aktywność
    elif xyz <= 3:
        x = int(input("Podaj swoją wagę:"))
        waga1 = (x * 10)
        y = int(input("Podaj swój wzrost w centymetrach:"))
        wzrost1 = (y * 6.25)
        z = int(input("Podaj swój wiek:"))
        wiek1 = (z * 5)
        wynik = int((waga1 + wzrost1 - wiek1) + 5)
        wynik1 = int(wynik * 1.5 - 500)
        print(str(wynik1) + "kcal" + " " + "Tyle kalorii potrzebujesz aby schudnąć! :)")
else:
    print("Powiedz mi jaką aktywność masz na codzień:")
    xyz = int(input("1 - Niska aktywność 2 - Średnia aktywność 3 - Wysoka aktywność:"))

    #   niska aktywność
    if xyz == 1:
        x = int(input("Podaj swoją wagę:"))
        waga1 = (x * 10)
        y = int(input("Podaj swój wzrost w centymetrach:"))
        wzrost1 = (y * 6.25)
        z = int(input("Podaj swój wiek:"))
        wiek1 = (z * 5)
        wynik = int((waga1 + wzrost1 - wiek1) + 5)
        wynik1 = int(wynik * 1.2 - 500)
        print(str(wynik1) + "kcal" + " " + "Tyle kalorii potrzebujesz aby schudnąć! :)")

    #   średnia aktywność
    elif xyz <= 2:
        x = int(input("Podaj swoją wagę:"))
        waga1 = (x * 10)
        y = int(input("Podaj swój wzrost w centymetrach:"))
        wzrost1 = (y * 6.25)
        z = int(input("Podaj swój wiek:"))
        wiek1 = (z * 5)
        wynik = int((waga1 + wzrost1 - wiek1) + 5)
        wynik1 = int(wynik * 1.4 - 500)
        print(str(wynik1) + "kcal" + " " + "Tyle kalorii potrzebujesz aby schudnąć! :)")

    # Wysoka aktywność
    elif xyz <= 3:
        x = int(input("Podaj swoją wagę:"))
        waga1 = (x * 10)
        y = int(input("Podaj swój wzrost w centymetrach:"))
        wzrost1 = (y * 6.25)
        z = int(input("Podaj swój wiek:"))
        wiek1 = (z * 5)
        wynik = int((waga1 + wzrost1 - wiek1) - 161)
        wynik1 = int(wynik * 1.5)
        print(str(wynik1) + "kcal" + " " + "Tyle kalorii potrzebujesz aby schudnąć! :)")