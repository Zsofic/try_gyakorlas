# 1. feladat
try:
    eletkor = int(input("Add meg az életkorodat: "))
    hatralevo = 100 - eletkor
    print("Ennyi év múlva leszel 100 éves:", hatralevo)
except ValueError:
    print("Számot adj meg!")


# 2. feladat
try:
    fajlnev = input("Add meg a fájl nevét: ")
    file = open(fajlnev, "r")

    try:
        elso_sor = file.readline()
        szam = float(elso_sor)
        print("A szám kétszerese:", szam * 2)
    except ValueError:
        print("A fájl első sora nem szám.")

    file.close()

except FileNotFoundError:
    print("Nem létezik ilyen nevű fájl.")


# 3. feladat
try:
    jelszo = input("Adj meg egy saját jelszót: ")

    if len(jelszo) < 8:
        raise Exception("A jelszó túl rövid! Minimum 8 karakter kell legyen.")

    print("Jelszó elfogadva.")

except Exception as hiba:
    print(hiba)