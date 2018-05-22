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
points = "+0"


def change_coordinates(x):  # ruch w poziomie: minus, w pionie: plus
    if x[-1] == "-":
        correct = "".join(x[1:-1] + x[0])
    else:
        correct = "".join((x[:-1]))
    return correct.upper()


def write_to_file(player_number):
    coordinates = ""
    points = ""
    letters = move[player_number].strip()[:-1].upper().replace("_", "?")  # porządkujemy ciag liter na stojaku
    if not move[player_number+1].isalpha() or move[player_number+1] == "P":  # czyli jeżeli nie ma wymiany,
        #  bo wtedy w tym elemencie mamy ciąg wymienianych liter
        coordinates = change_coordinates(move[player_number+1])
        if move[player_number+1] != "(C)" and move[player_number+1] != "P" and move[player_number+1] != "(T)" and move[player_number+1] != "(W)":
            # jeżeli wystąpił normalny ruch a nie wymiana etc.
            x = move[player_number+2].find("/")
            if x != -1:
                move_letters = move[player_number+2][:x]
            else:
                move_letters = move[player_number+2]
            points = move[player_number+3]
        else:
            coordinates = "-"
            move_letters = ""
    else:
        move_letters = "".join("-" + move[player_number+1])

    q = move_letters.find("[")
    move_letters = move_letters.upper()
    if q != -1:
        print(q)
        blank = move[player_number+2][q + 1]
        move_letters = "".join(move_letters[:q] + blank + move_letters[q + 3:])
    if player_number == 0:
        f2.write(">" + player2 + " " + letters + " " + coordinates + " " + move_letters + " " + points + "\n")
    else:
        f2.write(">" + player1 + " " + letters + " " + coordinates + " " + move_letters + " " + points + "\n")



for i in range(count - 4):
    move = f.readline().strip('\n').strip('\r').split(" ")  # wczytujemy linię z pominięciem znaków przejścia i dzielimy
    second_player = move[0].strip()[:-1].replace("_", "")  # drugi gracz ma dodatkowy element, wiec musimy ich rozroznic
    if second_player.isalpha():  # jeżeli pierwszym elementem jest ciąg liter a nie liczba, czyli w praktyce drugi gracz
        write_to_file(0)
    else:  # czyli pierwszy gracz danej kolejki
        write_to_file(1)
