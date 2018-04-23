import codecs

f = open("partia.txt")
f2 = codecs.open("przerobiona.txt", "w", "utf-8")
count = len(f.readlines())
f.close()
f = codecs.open('partia.txt', 'r', 'utf-8')
player1 = f.readline().split(" ")[1]
player2 = f.readline().split(" ")[1]
f2.write("#player1 " + player1 + " " + player1 + "\n")
f2.write("#player2 " + player2 + " " + player2 + "\n")
f.readline()
f.readline()
actually_move = ""


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


def change_coordinates(x):  # ruch w poziomie: minus, w pionie: plus
    if x[-1] == "-":
        correct = "".join(x[1:-1] + x[0])
    else:
        correct = "".join((x[:-1]))
    return correct.upper()


for i in range(count - 4):  # f.readline():
    points = "+0"
    move_letters = ""
    coordinates = ""
    move = f.readline().strip('\n').strip('\r').split(" ")  # wczytujemy linię z pominięciem znaków przejścia i dzielimy
    second_player = move[0].strip()[:-1].replace("_", "")  # drugi gracz ma dodatkowy element, wiec musimy ich rozroznic
    if second_player.isalpha():  # jeżeli pierwszym elementem jest ciąg liter a nie liczba, czyli w praktyce drugi gracz
        letters = move[0].strip()[:-1].upper().replace("_", "?")  # porządkujemy ciag liter na stojaku
        if not move[1].isalpha() or move[1] == "P":  # czyli jeżeli nie ma wymiany, bo wtedy w tym elemencie
            #  mamy ciąg wymienianych liter
            coordinates = change_coordinates(move[1])
            if move[1] != "(C)" and move[1] != "P" and move[1] != "(T)" and move[1] != "(W)":
                # jeżeli wystąpił normalny ruch a nie wymiana etc.
                x = move[2].find("/")
                if x != -1:
                    move_letters = move[2][:x]
                else:
                    move_letters = move[2]
                points = move[3]
            else:
                coordinates = "-"
        else:
            move_letters = "".join("-" + move[1])
        q = move_letters.find("[")
        move_letters = move_letters.upper()
        if q != -1:
            print(q)
            blank = move[2][q+1]
            move_letters = "".join(move_letters[:q] + blank + move_letters[q+3:])
        f2.write(">" + player2 + " " + letters + " " + coordinates + " " + move_letters + " " + points + "\n")
    else:  # czyli pierwszy gracz danej kolejki
        letters = move[1].strip()[:-1].upper().replace("_", "?")
        if not move[2].isalpha():
            coordinates = change_coordinates(move[2])
            if move[2] != "(C)" and move[2] != "P" and move[2] != "(T)" and move[2] != "(W)":
                # jeżeli wystąpił normalny ruch a nie wymiana etc.
                x = move[3].find("/")
                if x != -1:
                    move_letters = move[3][:x]
                else:
                    move_letters = move[3]
                points = move[4]
            else:
                coordinates = "-"
        else:
            move_letters = "".join("-" + move[2])
            points = "+0"
        q = move_letters.find("[")
        move_letters = move_letters.upper()
        if q != -1:
            print(q)
            blank = move[3][q+1]
            q = move_letters.find("[")
            move_letters = "".join(move_letters[:q] + blank + move_letters[q+3:])
        f2.write(">" + player1 + " " + letters + " " + coordinates + " " + move_letters + " " + points + "\n")
