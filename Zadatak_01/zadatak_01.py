# Unesi jedan broj


broj = int(input("Molim vas unesite jedan broj: "))
end = int(broj)

for n in range(1, end+1):
    for x in range(2, n):
        if n % x == 0:
            print(n, 'je prirodni broj')
            break
        else:
            print(n, 'je prim broj!')
            break


