import numpy as np


class Ruch:
    def __init__(self, wsp, s):
        self.orientacja = 0
        self.wsp = wsp
        self.wylozonePlytki = s
        self.konwertujWspolrzedne()

    def konwertujWspolrzedne(self):
        if self.wsp[0] == "1" or self.wsp[0] == "0":
            self.wspX = zmianaWspolrzednych(self.wsp[2])
            self.wspY = int(self.wsp[0:2])-1
            self.orientacja = 1
        else:
            self.wspX = zmianaWspolrzednych(self.wsp[0])
            self.wspY = int(self.wsp[1:3])-1


premieSlowne = np.zeros((15, 15), dtype=int)
punktacjaLiter = {
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
premieSlowne[(0, 0)] = 3
premieSlowne[(0, 7)] = 3
premieSlowne[(0, 14)] = 3
premieSlowne[(7, 0)] = 3
premieSlowne[(7, 14)] = 3
premieSlowne[(14, 0)] = 3
premieSlowne[(14, 7)] = 3
premieSlowne[(7, 7)] = 2
premieSlowne[(14, 14)] = 3
for i in range(1, 5):
        premieSlowne[(i, i)] = 2
        premieSlowne[(i, 14 - i)] = 2
        premieSlowne[(14 - i, i)] = 2
        premieSlowne[(14 - i, 14 - i)] = 2
print(premieSlowne)
plansza = np.zeros((15, 15), dtype=str)
print(plansza)
def liczeniePremiiSlownych(ruch):
    sum = 0
    x = ruch.wspX
    y = ruch.wspY
    for a, i in enumerate(ruch.wylozonePlytki):
        if ruch.orientacja == 1:
            sum += premieSlowne[(x+a, y)]
        else :
            sum += premieSlowne[(x, y+a)]
    print("suma premii słownych:", sum)
    return sum


def zmianaWspolrzednych(a):
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


def dodajSlowo(klasa):
    slowo = klasa.wylozonePlytki.upper()
    x = klasa.wspX
    y = klasa.wspY
    o = klasa.orientacja
    for litera in slowo:
        plansza[(x, y)] = litera
        if o == 0:
            y += 1
        else:
            x += 1


def czySieKrzyzuje(ruch):
    noweSlowo = ruch.wylozonePlytki
    x = ruch.wspX
    y = ruch.wspY
    for i, j in enumerate(noweSlowo):
        print (x, y, str(plansza[(x, y)]))
        if plansza[(x, y)]:
            return False
        print(i, j)
        if plansza[(x+i, y-1)] or plansza[(x+i, y+1)] or plansza[(x, y+i)] or plansza[(x, y-i)] or plansza[(x - 1, y + i)] or plansza[(x + 1, y + i)] or plansza[(x, y+1)] or plansza[(x, y-1)]:
            return True
    return False
#x = 2, y = 1

def sprawdzPowstaleSlowa(ruch):
    x = ruch.wspX
    y = ruch.wspY
    list = []
    string = ""
    if ruch.orientacja == 1:
        while plansza[(x, y)]:
            x -= 1
        x += 1
        while plansza[(x, y)]:
            string += str(plansza[(x, y)])
            x += 1
        if string.__len__() > 1:
            list.append(string)
        x = ruch.wspX
        y = ruch.wspY
        for i in ruch.wylozonePlytki:
            string = ""
            while plansza[(x, y)]:
                y -= 1
            y += 1
            while plansza[(x, y)]:
                string += str(plansza[(x, y)])
                y += 1
            if string.__len__() > 1:
                list.append(string)
            x += 1
            y = ruch.wspY
    else:
        while plansza[(x, y)]:
            y -= 1
        y += 1
        while plansza[(x, y)]:
            string += str(plansza[(x, y)])
            y += 1
        if string.__len__() > 1:
            list.append(string)
        x = ruch.wspX
        y = ruch.wspY
        for i in ruch.wylozonePlytki:
            string = ""
            while plansza[(x, y)]:
                x -= 1
            x += 1
            while plansza[(x, y)]:
                string += str(plansza[(x, y)])
                x += 1
            if string.__len__() > 1:
                list.append(string)
            y += 1
            x = ruch.wspX

    print(list)


wspolrzedne = "04c"     ##input("słowo zaczyna się od:")
slowo = "GŻegŻÓŁKA".upper()
pierwszy = Ruch(wspolrzedne, slowo)
drugi = Ruch("b11", "lama")
trzeci = Ruch("03b", "kot")
czwarty = Ruch("02c", "j")
piaty = Ruch("03e", "eria")
punktySlowa = 0
for i in slowo:
    punktySlowa += punktacjaLiter[i]
print("wartość punktowa słowa: " + str(punktySlowa*liczeniePremiiSlownych(pierwszy)))
dodajSlowo(pierwszy)
dodajSlowo(drugi)
poprawnie = czySieKrzyzuje(trzeci)
dodajSlowo(trzeci) if poprawnie else print("nie można dodać bo się nie krzyżuje")
sprawdzPowstaleSlowa(trzeci)
poprawnie = czySieKrzyzuje(czwarty)
dodajSlowo(czwarty) if poprawnie else print("nie można dodać bo się nie krzyżuje")
sprawdzPowstaleSlowa(czwarty)
dodajSlowo(piaty) if czySieKrzyzuje(piaty) else print("nie można dodać bo się nie krzyżuje")
sprawdzPowstaleSlowa(piaty)
print(plansza)