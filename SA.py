import numpy as np

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
def liczeniePremiiSlownych(x, y, l, o):
    sum = 0
    for a in range(l):
        if o == 0:
            sum += premieSlowne[(x+a, y)]
        else :
            sum += premieSlowne[(x, y+a)]
    print("sum:", sum)
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


def dodajSlowo(slowo, x, y, o):
    slowo = slowo.upper()
    for litera in slowo:
        plansza[(x, y)] = litera
        if o == 0:
            y += 1
        else:
            x += 1


def czySieKrzyzuje(noweSlowo, x, y):
        for i,j in enumerate(noweSlowo):
            print(i,j)
            if plansza[(x+i, y-1)] or plansza[(x+i, y+1)] or plansza[(x, y+i) or plansza[(x, y-i)]]:
                return True
        return False


wspolrzedne = "04c"     ##input("słowo zaczyna się od:")
if wspolrzedne[0] == "1" or wspolrzedne[0] == "0":
    startSlowaX = zmianaWspolrzednych(wspolrzedne[2])
    startSlowaY = int(wspolrzedne[0:2])
    o = 1
else:
    startSlowaX = zmianaWspolrzednych(wspolrzedne[0])
    startSlowaY = int(wspolrzedne[1:3])
    o = 0
slowo = "GŻegŻÓŁKA".upper()
punktySlowa = 0
for i in slowo:
    punktySlowa += punktacjaLiter[i]
print(punktySlowa)
print(startSlowaX, startSlowaY, o, liczeniePremiiSlownych(startSlowaX, startSlowaY-1, slowo.__len__(), o))
print("wartość punktowa słowa: " + str(punktySlowa*liczeniePremiiSlownych(startSlowaX, startSlowaY-1, slowo.__len__(), o)))
dodajSlowo(slowo,startSlowaX,startSlowaY-1,o)
dodajSlowo("poń",4,5,0)
print(plansza)
slowo2 = "nowe".upper()
wspolrzedne2x=0
wspolrzedne2y=7
poprawnie = czySieKrzyzuje(slowo2, wspolrzedne2x, wspolrzedne2y)
dodajSlowo(slowo2, wspolrzedne2x, wspolrzedne2y, 1) if poprawnie else print("nie można dodać bo się nie krzyżuje")
print(plansza)

wspolrzedne2x=8
wspolrzedne2y=3
poprawnie = czySieKrzyzuje(slowo2, wspolrzedne2x, wspolrzedne2y)
dodajSlowo(slowo2, wspolrzedne2x, wspolrzedne2y, 0) if poprawnie else print("nie można dodać bo się nie krzyżuje")
print(plansza)
