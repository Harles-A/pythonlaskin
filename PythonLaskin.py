def laskin():

    # Kysy mit� henkil� haluaa tehd�
    laskelma = input('''
    Valitse suorittettavan matemaattisen toiminnon tyyppi: 
    + Yhteenlasku
    - V�hennyslasku
    * Kertolasku
    / Jakolasku
    % Jakoj��nn�s
    ''')

    # Tallentaa numerot muuttujiin
    numero_1 = float(input("Sy�t� ensimm�inen numero: "))
    numero_2 = float(input("Sy�t� toinen numero: "))


# Yhteenlasku
    if laskelma == "+":
        print("{} + {} = ".format(numero_1, numero_2))
        print(numero_1 + numero_2)

    # V�hennyslasku
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

    # Jakoj��nn�s
    elif laskelma == "%":
        print("{} % {} = ".format(numero_1, numero_2))
        print(numero_1 % numero_2)
    # Jos valinta oli alussa virheellinen
    else: 
        print("Et valinnut kelvollista laskutoimitusta.")
    # Kysy, haluaako henkil� laskea uudelleen
    uudestaan()
    # Funktio miss� kysytt��n haluaako henkil� laskea uudelleen
def uudestaan():

    laske_uudestaan = input('''
    Haluatko laskea uudestaan?
    Kirjoita joo, jos haluat, tai ei, jos et.
    ''')

    # Muuntaa vastaukset isoiksi(.upper), ongelmien v�ltt�miseksi
    if laske_uudestaan.upper() == "JOO":
        laskin()

    elif laske_uudestaan.upper() == "EI":
        print("Hyv�sti!")

    else:
        uudestaan()

laskin()
