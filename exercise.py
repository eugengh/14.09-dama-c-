a = int(input('a = '))
b = int(input('b = '))
def suma(a, b):
    return print(a+b)

def produs(a, b):
    return print(a*b)

def media(a, b):
    return print('Media aritm = ', a+b/2)

def divizor(a, b):
    diva = []
    divb = []
    divab = []
    for i in range(1, a+1):
        if a%i ==0:
            diva.append(i)
    for x in range(1, b+1):
        if b%x == 0:
            divb.append(x)
    for m in diva:
        for n in divb:
            if m == n:
                divab.append(m)
    return print(max(divab))

def multiplu(a ,b):
    mula = []
    mulb = []
    mulab = []
    mula =(list(range(a, 15*a, a)))
    mulb =(list(range(b, 15*b, b)))
    for i in mula:
        for x in mulb:
            if i == x:
                mulab.append(i)
    return print(min(mulab))

def comparatie(a, b):
    c = 0
    if a > b:
        return print('Nr maxim este'+str(a)+ ', iar nr minim este' + str(b))
    if b > a:
        return print('Nr maxim este'+str(b)+ ', iar nr minim este' + str(a))

def sums(a, b):
    c= a+b
    return print('a + b =', c,)

def prods(a, b):
    c = a*b
    return print('a * b =', c,)

def divizorc(a, b):
    diva = []
    divb = []
    divab = []
    for i in range(1, a+1):
        if a%i ==0:
            diva.append(i)
    for x in range(1, b+1):
        if b%x == 0:
            divb.append(x)
    for m in diva:
        for n in divb:
            if m == n:
                divab.append(m)
    return print(divab)

def multiplu(a ,b):
    mula = []
    mulb = []
    mulab = []
    mula =(list(range(a, 150*a, a)))
    mulb =(list(range(b, 150*b, b)))
    for i in mula:
        for x in mulb:
            if i == x:
                mulab.append(i)
    return print(mulab[0:5])

def cifre(a ,b):
    ada=[]
    for i in str(a):
        for x in str(b):
            if x==i:
                ada.append(i)
    return print(list(dict.fromkeys(ada)))
                
def cifre(a ,b):
    ada=[]
    for i in str(a):
        if str(b).__contains__(i) == False:
            ada.append(i)
    return print(ada)

def prieten(a, b):
    diva = []
    divb = []
    for i in range(1, a+1):
        if a%i ==0:
            diva.append(i)
    for x in range(1, b+1):
        if b%x == 0:
            divb.append(x)
    if len(diva) == len(divb):
        return print('Nr', a,'si', b,' sunt prietene')
    else:
        return print('Nr', a,'si', b,' nu sunt prietene')