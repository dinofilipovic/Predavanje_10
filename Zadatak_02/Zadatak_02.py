import random as rnd

while True:
    broj = rnd.randint(1, 1000)
    print("Random broj je: ", broj)

    for x in range(2, broj+1):
        if broj % x == 0:
            print(broj, 'je prosti broj!')
            exit()
            break
        else:
            print(broj, 'je primarni broj!')
            break
