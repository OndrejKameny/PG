def cislo_text(cislo):
    cislo=int(cislo)

    jednotky=["nula","jedna","dva","tři","čtyři","pět","šest","sedm","osm","devět"]
    nact=["deset","jedenáct","dvanáct","třináct","čtrnáct","patnáct","šestnáct","sedmnáct","osmnáct","devatenáct"]
    desitky=["","","dvacet","třicet","čtyřicet","padesát","šedesát","sedmdesát","osmdesát","devadesát"]

    if cislo<10:
        return jednotky[cislo]
    elif cislo<20:
        return nact[cislo-10]
    elif cislo<100:
        des=cislo//10
        jed=cislo % 10
        if jed == 0:
            return desitky[des]
        else:
            return desitky[des] + " " + jednotky[jed]
    elif cislo==100:
        return "sto"
    else:
        return "mimo rozsah"
    
if __name__ == "__main__":
    cislo=input("Zadej cislo")
    text=cislo_text(cislo)
    print(text)