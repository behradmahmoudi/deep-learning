def XOR(x1, x2):
    z11 = 2*x1 -x2 -2
    if z11 >= 0:
        z1 = 1
    else:
        z1 = 0
    z22 = -x1 + 2*x2 -2
    if z22 >= 0:
        z2 = 1
    else:
        z2 = 0
    y = 2*z1 + 2*z2 -2
    if y >= 0:
        return 1
    else:
        return 0
def AND(x1,x2):
    z11 = x1 +x2 -2
    if z11 >= 0:
        return 1
    else:
        return 0
def OR(x1,x2):
    z11 = 2*x1 + 2*x2 - 2
    if z11 >= 0:
        return 1
    else:
        return 0
def HALFADDER(x1,x2):
    C = AND(x1,x2)
    S = XOR(x1,x2)
    return C, S
def FULLADDER(x1,x2,cin):
    E = XOR(x1,x2)
    S = XOR(E,cin)
    D = AND(E,cin)
    F = AND(x1,x2)
    COUT = OR(D,F)
    return COUT, S
for a0 in [0,1]:
    for a1 in [0,1]:
        for b0 in [0,1]:
            for b1 in [0,1]:
                COUT0, ST0 = HALFADDER(a0, b0)
                COUT1, ST1 = FULLADDER(a1, b1, COUT0)
                print('%d%d plus %d%d is %d%d%d'%(a1, a0, b1, b0, COUT1, ST1,ST0))








