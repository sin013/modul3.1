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


def IsContains(a, b):
    global cals
    i = False
    a = a.upper()
    for j in b:
        if j.upper() == a:
            i = True
        else:
            i = False

    print(i)
    CountCalls()


StringInfo('gdfkl')
StringInfo('str(input())')
StringInfo("jfbfdhj")
IsContains("bfdb", ['dsfugdsf', 'sdgjshhkds'])
IsContains('sudgdufg', ["UrbaN", "dfbjgjsbgj"])
IsContains("urban", ['sdgihi', 'URbaN'])
print(cals)
