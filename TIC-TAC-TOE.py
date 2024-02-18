def mir (n=3, m=3):
    a = []
    for i in range(n):
        a.append(["-"] * m)
    return a
def normalmir (a):
    for i in a:
        print(*i)
def hod (j):
    x,y = map(int,input().split())
    while a[x-1][y-1]!='-':
        print("Эта ячейка уже занята")
        x, y = map(int, input().split())
    a[x-1][y-1] = j
def result():
    for i in range (len(a)):
        if a[i][0]==a[i][1]==a[i][2] and a[i][0]!="-":
            return a[i][0]
    for j in range (len(a)):
        if a[0][j] == a[1][j] == a[2][j] and a[0][j] != "-":
            return a[0][j]
    if a[0][0]==a[1][1]==a[2][2] and a[0][0] != "-":
        return a[0][0]
    if a[0][2]==a[1][1]==a[2][0] and a[2][0] != "-":
        return a[0][2]
    if "-" not in a[0] and "-" not in a[1] and "-" not in a[2]:
        return True
    return False
def pobeda ():
    c = result()
    if c == True:
        print ("Ничья")
        input()
        exit ()
    elif c != False:
        print("Победили", c)
        normalmir(a)
        input()
        exit ()
def robot ():
    import random
    gg = [0, 1, 2]
    x,y = smartturns("o")
    while a[x][y]!='-':
        x, y = smartturns("o")
    a[x][y] = 'o'
def combinations ():
    combs = []
    for i in range (len(a)):
        winstrategy = []
        for j in range (len(a[i])):
            winstrategy.append ((i,j))
        combs.append (winstrategy)
    for j in range (len(a)):
        winstrategy = []
        for i in range (len(a[j])):
            winstrategy.append ((i,j))
        combs.append (winstrategy)
    combs.append ([(0,0),(1,1),(2,2)])
    combs.append ([(0,2),(1,1),(2,0)])
    return combs
def smartturns (symbol):
    import random
    combs = combinations()
    allznacheniya = []
    for i in range (len(combs)):
        znacheniya = []
        for j in range (len(combs[i])):
            znacheniya.append(a[combs[i][j][0]][combs[i][j][1]])
        allznacheniya.append(znacheniya)
    for i in range (len(allznacheniya)):
        if allznacheniya[i].count(symbol) == 2 and '-' in allznacheniya[i]:
            l = allznacheniya[i].index('-')
            return combs[i][l]
    for i in range (len(allznacheniya)):
        if allznacheniya[i].count(symbol) == 0 and allznacheniya[i].count('-')==1:
            l = allznacheniya[i].index('-')
            return combs[i][l]
    for i in range (len(allznacheniya)):
        if allznacheniya[i].count(symbol) == 1 and allznacheniya[i].count('-')==2:
            l = allznacheniya[i].index('-')
            return combs[i][l]
    gg = [0, 1, 2]
    x = random.choice(gg)
    y = random.choice(gg)
    return x,y
menu = input("Введите количество игроков ").strip()
if menu == "1":
    a = mir()
    normalmir(a)
    while True:
        hod("x")
        pobeda()
        robot()
        normalmir(a)
        pobeda()
else:
    a = mir()
    normalmir(a)
    while True:
        hod("x")
        pobeda()
        hod("o")
        normalmir(a)
        pobeda()
