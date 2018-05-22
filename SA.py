import numpy as np
import codecs

punktacja_liter = {
        'A': 1,
        'Ą': 5,
        'B': 3,
        'C': 2,
        'Ć': 6,
        'D': 2,
        'E': 1,
        'Ę': 5,
        'F': 5,
        'G': 3,
        'H': 3,
        'I': 1,
        'J': 3,
        'K': 2,
        'L': 2,
        'Ł': 3,
        'M': 2,
        'N': 1,
        'Ń': 7,
        'O': 1,
        'Ó': 5,
        'P': 2,
        'R': 1,
        'S': 1,
        'Ś': 5,
        'T': 2,
        'U': 3,
        'W': 1,
        'Y': 2,
        'Z': 1,
        'Ź': 9,
        'Ż': 5}
premie_slowne = np.zeros((15, 15), dtype=int)
premie_literowe = np.zeros((15, 15), dtype=int)
plansza = np.zeros((15, 15), dtype=str)
plansza_tymczasowa = np.zeros((15, 15), dtype=str)

def wypelnij_premie():
    premie_slowne[(0, 0)] = 3
    premie_slowne[(0, 7)] = 3
    premie_slowne[(0, 14)] = 3
    premie_slowne[(7, 0)] = 3
    premie_slowne[(7, 14)] = 3
    premie_slowne[(14, 0)] = 3
    premie_slowne[(14, 7)] = 3
    premie_slowne[(7, 7)] = 2
    premie_slowne[(14, 14)] = 3
    for a in range(1, 5):
        premie_slowne[(a, a)] = 2
        premie_slowne[(a, 14 - a)] = 2
        premie_slowne[(14 - a, a)] = 2
        premie_slowne[(14 - a, 14 - a)] = 2
    premie_literowe[(0, 3)] = 2
    premie_literowe[(0, 11)] = 2
    premie_literowe[(3, 0)] = 2
    premie_literowe[(11, 0)] = 2
    premie_literowe[(3, 14)] = 2
    premie_literowe[(11, 14)] = 2
    premie_literowe[(14, 3)] = 2
    premie_literowe[(14, 11)] = 2


wypelnij_premie()


class Ruch:

    def __init__(self, wsp, plytki):
        self.pionowo = False
        self.wsp = wsp
        self.wylozone_plytki = plytki
        self.konwertuj_wspolrzedne()

    def konwertuj_wspolrzedne(self):
        if self.wsp[0] == "1" or self.wsp[0] == "0":
            self.wspX = zmiana_wspolrzednych(self.wsp[2])
            self.wspY = int(self.wsp[0:2])-1
            self.pionowo = True
        else:
            self.wspX = zmiana_wspolrzednych(self.wsp[0])
            self.wspY = int(self.wsp[1:3])-1


slownik = set()
s = codecs.open("slownikdo7.txt", "r", "utf-8")
slowo = s.readline().strip()
slownik.add(slowo)
while slowo:
    slowo = s.readline().strip()
    slownik.add(slowo)


def liczenie_premii_slownych(ruch):
    suma = 0
    x = ruch.wspX
    y = ruch.wspY
    for a in range(len(ruch.wylozone_plytki)):
        if ruch.pionowo:
            suma += premie_slowne[(x + a, y)]
        else:
            suma += premie_slowne[(x, y + a)]
    print("suma premii słownych:", suma)
    return suma


def zmiana_wspolrzednych(a):
    if a == "a":
        return 0
    if a == "b":
        return 1
    if a == "c":
        return 2
    if a == "d":
        return 3
    if a == "e":
        return 4
    if a == "f":
        return 5
    if a == "g":
        return 6
    if a == "h":
        return 7
    if a == "i":
        return 8
    if a == "j":
        return 9
    if a == "k":
        return 10
    if a == "l":
        return 11
    if a == "m":
        return 12
    if a == "n":
        return 13
    if a == "o":
        return 14


def dodaj_slowo(klasa):  # dodaje słowo na planszę
    slowo_do_dodania = klasa.wylozone_plytki.upper()
    x = klasa.wspX
    y = klasa.wspY
    o = klasa.pionowo
    for l in slowo_do_dodania:
        print("x, y:", x, y)
        plansza_tymczasowa[(x, y)] = l
        if not o:
            y += 1
        else:
            x += 1


def sprawdz_czy_sie_krzyzuje(ruch):
    nowe_slowo = ruch.wylozone_plytki
    x = ruch.wspX
    y = ruch.wspY
    for l in range(len(nowe_slowo)):
        if plansza[(x, y)]:
            return False
        if plansza[(x + l, y - 1)] or plansza[(x + l, y + 1)] or plansza[(x, y + l)] or plansza[(x, y - l)] \
                or plansza[(x - 1, y + l)] or plansza[(x + 1, y + l)] or plansza[(x, y + 1)] or plansza[(x, y - 1)]:
            return True
    return False
#  x = 2, y = 1


print(type(plansza_tymczasowa[(1, 1)]), type(5))


def sprawdz_powstale_slowa(ruch):
    x = ruch.wspX
    y = ruch.wspY
    powstale_slowa = []
    string = ""
    if ruch.pionowo:
        while plansza_tymczasowa[(x, y)]:
            x -= 1
        x += 1
        while plansza_tymczasowa[(x, y)]:
            string += str(plansza_tymczasowa[(x, y)])
            x += 1
        if string.__len__() > 1:
            powstale_slowa.append(string)
        x = ruch.wspX
        y = ruch.wspY
        for _ in ruch.wylozone_plytki:
            string = ""
            while plansza_tymczasowa[(x, y)]:
                y -= 1
            y += 1
            while plansza_tymczasowa[(x, y)]:
                string += str(plansza_tymczasowa[(x, y)])
                y += 1
            if string.__len__() > 1:
                powstale_slowa.append(string)
            x += 1
            y = ruch.wspY
    else:
        while plansza_tymczasowa[(x, y)]:
            y -= 1
        y += 1
        while plansza_tymczasowa[(x, y)]:
            string += str(plansza_tymczasowa[(x, y)])
            y += 1
        if string.__len__() > 1:
            powstale_slowa.append(string)
        x = ruch.wspX
        y = ruch.wspY
        for _ in ruch.wylozone_plytki:
            string = ""
            while plansza_tymczasowa[(x, y)]:
                x -= 1
            x += 1
            while plansza_tymczasowa[(x, y)]:
                string += str(plansza_tymczasowa[(x, y)])
                x += 1
            if string.__len__() > 1:
                powstale_slowa.append(string)
            y += 1
            x = ruch.wspX

    print(powstale_slowa)
    for slowo_w_osps in powstale_slowa:
        if slowo_w_osps in slownik:
            print("slowo {} jest w słowniku".format(slowo_w_osps))
        else:
            print("słowa {} nie ma w słowniku".format(slowo_w_osps))
            return False
    return True


def czysc_plansze():
    plansza_tymczasowa[:][:] = plansza[:][:]


def aktualizuj_plansze():
    plansza[:][:] = plansza_tymczasowa[:][:]


ruchy = []
wspolrzedne = "04c"  # input("słowo zaczyna się od:")
slowo = "GŻegŻÓŁKA".upper()
ruchy.append(Ruch(wspolrzedne, slowo))
ruchy.append(Ruch("b11", "lama"))
ruchy.append(Ruch("03b", "kot"))
ruchy.append(Ruch("02c", "j"))
ruchy.append(Ruch("03e", "eria"))


punkty_slowa = 0
for i in slowo:
    punkty_slowa += punktacja_liter[i]
print("wartość punktowa słowa: " + str(punkty_slowa * liczenie_premii_slownych(ruchy[0])))
dodaj_slowo(ruchy[0])
aktualizuj_plansze()
for r in ruchy:
    dodaj_slowo(r) if sprawdz_czy_sie_krzyzuje(r) else print("nie można dodać bo się nie krzyżuje")
    if sprawdz_powstale_slowa(r):
        print("wszystko ok")
        aktualizuj_plansze()
    czysc_plansze()

litera = 'topos'
generowany = Ruch("01a", litera)
generowany.wylozone_plytki = litera
for i in range(15):
    for j in range(15):
        if i + len(litera) < 15 and j + len(litera) < 15:
            generowany.wspY = j
            generowany.wspX = i
        else:
            continue
        dodaj_slowo(generowany) if sprawdz_czy_sie_krzyzuje(generowany) else ""
        if sprawdz_powstale_slowa(generowany):
            print("wszystko ok")
            aktualizuj_plansze()
        czysc_plansze()


print(plansza)
