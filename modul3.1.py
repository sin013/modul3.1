cals = 0


def CountCalls():
    global cals
    cals += 1


def StringInfo(a):
    global cals
    s = (len(a), (a.upper()), a.lower())
    s = (tuple(s))
    print(s)
    CountCalls()


def IsContains(a):
    global cals
    a = a.upper()
    if a == 'URBAN':
        a = True
    else:
        a = False
    print(a)
    CountCalls()


StringInfo('gdfkl')
StringInfo('str(input())')
StringInfo("jfbfdhj")
IsContains("bfdb")
IsContains("UrbaN")
IsContains("urban")
print(cals)
