def je_tah_mozny(figurka, cilova_pozice, obsazene_pozice):
    typ = figurka.get("typ")
    pozice = figurka.get("pozice")
    if pozice is None or typ is None:
        return False

    r0, c0 = pozice
    r1, c1 = cilova_pozice

    # 1) Ověřte, jestli cilova_pozice neni mimo šachovnici
    if not (1 <= r1 <= 8 and 1 <= c1 <= 8):
        return False

    # 2) Ověřte, zda je daná pozice volná
    if (r1, c1) in obsazene_pozice:
        return False

    dr = r1 - r0
    dc = c1 - c0
    abs_dr = abs(dr)
    abs_dc = abs(dc)

    # 3) Ověřte, zda je pro danou figuru tato pozice přípustná (vzhledem k pohybu figur)
    def cesta_je_volna(step_r, step_c):
        r, c = r0 + step_r, c0 + step_c
        while (r, c) != (r1, c1):
            if (r, c) in obsazene_pozice:
                return False
            r += step_r
            c += step_c
        return True

    if typ == "pěšec":
        # pohyb pouze dopředu (zvýšení řady)
        # 1 pole dopředu
        if dc == 0 and dr == 1:
            return True
        # 2 pole dopředu z výchozí pozice
        if dc == 0 and dr == 2 and r0 == 1:
            # zajistit, že mezi nimi není žádná figurka
            if (r0 + 1, c0) in obsazene_pozice:
                return False
            return True
        return False

    if typ == "jezdec":
        # L-tvar: 2 v jednom směru a 1 v druhém
        if (abs_dr, abs_dc) in [(1, 2), (2, 1)]:
            return True
        return False

    if typ == "věž":
        # horizontálně nebo vertikálně o libovolný počet a cesta volná
        if r0 == r1 and c0 != c1:
            step_c = 1 if c1 > c0 else -1
            return cesta_je_volna(0, step_c)
        if c0 == c1 and r0 != r1:
            step_r = 1 if r1 > r0 else -1
            return cesta_je_volna(step_r, 0)
        return False

    if typ == "střelec":
        # diagonálně o libovolný počet a cesta volná
        if abs_dr == abs_dc and abs_dr != 0:
            step_r = 1 if r1 > r0 else -1
            step_c = 1 if c1 > c0 else -1
            return cesta_je_volna(step_r, step_c)
        return False

    if typ == "dáma":
        # kombinace věže a střelce
        if r0 == r1 and c0 != c1:
            step_c = 1 if c1 > c0 else -1
            return cesta_je_volna(0, step_c)
        if c0 == c1 and r0 != r1:
            step_r = 1 if r1 > r0 else -1
            return cesta_je_volna(step_r, 0)
        if abs_dr == abs_dc and abs_dr != 0:
            step_r = 1 if r1 > r0 else -1
            step_c = 1 if c1 > c0 else -1
            return cesta_je_volna(step_r, step_c)
        return False

    if typ == "král":
        # o jedno pole v libovolném směru
        if max(abs_dr, abs_dc) == 1 and not (abs_dr == 0 and abs_dc == 0):
            return True
        return False

    # pokud nezná typ figurky
    return False
if __name__ == "__main__":
    pesec = {"typ": "pěšec", "pozice": (2, 2)}
    jezdec = {"typ": "jezdec", "pozice": (3, 3)}
    vez = {"typ": "věž", "pozice": (8, 8)}
    strelec = {"typ": "střelec", "pozice": (6, 3)}
    dama = {"typ": "dáma", "pozice": (8, 3)}
    kral = {"typ": "král", "pozice": (1, 4)}
    obsazene_pozice = {(2, 2), (8, 2), (3, 3), (5, 4), (8, 3), (8, 8), (6, 3), (1, 4)}

    print(je_tah_mozny(pesec, (3, 2), obsazene_pozice))  
    print(je_tah_mozny(pesec, (4, 2), obsazene_pozice))  
    print(je_tah_mozny(pesec, (1, 2), obsazene_pozice))  

    print(je_tah_mozny(jezdec, (4, 4), obsazene_pozice))  
    print(je_tah_mozny(jezdec, (5, 4), obsazene_pozice))  
    print(je_tah_mozny(jezdec, (1, 5), obsazene_pozice))  
    print(je_tah_mozny(jezdec, (9, 3), obsazene_pozice))  

    print(je_tah_mozny(dama, (8, 5), obsazene_pozice))  
    print(je_tah_mozny(dama, (1, 3), obsazene_pozice))  
    print(je_tah_mozny(dama, (3, 8), obsazene_pozice))  