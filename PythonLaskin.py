def laskin():

    # Kysy mitä henkilö haluaa tehdä
    laskelma = input('''
    Valitse suorittettavan matemaattisen toiminnon tyyppi: 
    + Yhteenlasku
    - Vähennyslasku
    * Kertolasku
    / Jakolasku
    % Jakojäännös
    ''')

    # Tallentaa numerot muuttujiin
    numero_1 = float(input("Syötä ensimmäinen numero: "))
    numero_2 = float(input("Syötä toinen numero: "))


# Yhteenlasku
    if laskelma == "+":
        print("{} + {} = ".format(numero_1, numero_2))
        print(numero_1 + numero_2)

    # Vähennyslasku
    elif laskelma == "-":
        print("{} - {} = ".format(numero_1, numero_2))
        print(numero_1 - numero_2)

    # Kertolasku
    elif laskelma == "*":
        print("{} * {} = ".format(numero_1, numero_2))
        print(numero_1 * numero_2)

    # Jakolasku
    elif laskelma == "/":
        print("{} / {} = ".format(numero_1, numero_2))
        print(numero_1 / numero_2)

    # Jakojäännös
    elif laskelma == "%":
        print("{} % {} = ".format(numero_1, numero_2))
        print(numero_1 % numero_2)
    # Jos valinta oli alussa virheellinen
    else: 
        print("Et valinnut kelvollista laskutoimitusta.")
    # Kysy, haluaako henkilö laskea uudelleen
    uudestaan()
    # Funktio missä kysyttään haluaako henkilö laskea uudelleen
def uudestaan():

    laske_uudestaan = input('''
    Haluatko laskea uudestaan?
    Kirjoita joo, jos haluat, tai ei, jos et.
    ''')

    # Muuntaa vastaukset isoiksi(.upper), ongelmien välttämiseksi
    if laske_uudestaan.upper() == "JOO":
        laskin()

    elif laske_uudestaan.upper() == "EI":
        print("Hyvästi!")

    else:
        uudestaan()

laskin()
