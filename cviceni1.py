
def delitelne_bez_zbytku3(cislo):
    if cislo % 3 == 0:
        return True
    return False

if __name__ == "__main__":
    if delitelne_bez_zbytku3(3):
        print("ano, je delitelne beze zbytku")
    else:
        print("neni delitelne beze zbytku")
    