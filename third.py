def je_prvocislo(cislo):
    if cislo < 2:
        return False
    for i in range(2, int(cislo ** 0.5) + 1):
        if cislo % i == 0:
            return False
    return True

def vrat_prvocisla(cislo2):
    prvocisla=[]
    for i in range(2, cislo2 + 1):
        if je_prvocislo(i):
            prvocisla.append(i)
    return prvocisla

if __name__ == "__main__":
    cislo2 = int(input("Zadej maximum: "))
    prvocisla = vrat_prvocisla(cislo2)
    print(prvocisla)