import random as rnd

secret = rnd.randint(1, 1)
attempts = 0

while True:
    guess = int(input("Pgodite tajni broj (od 1 do 30): "))
    attempts += 1

    if guess == secret:
        print("Pogodili ste! To je broj: " + str(secret))
        break;
    elif guess > secret:
        print("Preveliki broj!")
    elif guess < secret:
        print("Premali broj!")

with open("score.txt", "a") as score_file:
    score_file.write(str("{0}\n").format(attempts))
    score_file.close()

with open("score.txt", "r") as score_file:
    best_score = score_file.read()
    score_file.close()

def provjeraLinija(dokument):
    file = open(dokument, "r")
    linija = file.readline()
    while linija:
        vrijednost = linija.split()
        print('Linija: ', vrijednost)
        linija = file.readline()

    file.close()

provjeraLinija("score.txt")

exit()