def cislo_text(cislo):
    cislo = int(cislo)

    jednotky = ["nula", "jedna", "dva", "tři", "čtyři", "pět", "šest", "sedm", "osm", "devět"]

    if cislo < 10:
        return jednotky[cislo]

    if cislo == 100:
        return "sto"

    if cislo < 20:
        texty = ["deset", "jedenáct", "dvanáct", "třináct", "čtrnáct", "patnáct", "šestnáct", "sedmnáct", "osmnáct", "devatenáct"]
        return texty[cislo - 10]

    desitky = ["", "", "dvacet", "třicet", "čtyřicet", "padesát", "šedesát", "sedmdesát", "osmdesát", "devadesát"]

    if cislo % 10 == 0:
        return desitky[cislo // 10]

    return desitky[cislo // 10] + " " + jednotky[cislo % 10]


if __name__ == "__main__":
    cislo = input("Zadej číslo: ")
    text = cislo_text(cislo)
    print(text)