def sudy_nebo_lichy(cislo):
    if cislo % 2 == 0:
        print("Číslo", cislo, "je sudé.")
    else:
        print("Číslo", cislo, "je liché.")

print(sudy_nebo_lichy(5))
print(sudy_nebo_lichy(1000000))