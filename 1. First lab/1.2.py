n = int(input("Enter the number of rows:"))

spaces = n - 1

for i in range(1, n+1):
    for j in range(0, spaces):
        print(' ', end='')

    C = 1
    for j in range(1, i+1):
        if C % 2 == 1:
            print(' *', sep='', end='')
        else:
            print('  ', sep='', end='')
        C = C * (i - j) // j
    print()
    spaces -= 1