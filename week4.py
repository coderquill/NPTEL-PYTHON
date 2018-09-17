adict = {'match1':{'player1':57, 'player2':38},
        'match2':{'player3':9, 'player1':42},
        'match3':{'player2':41, 'player4':63, 'player3':91}}

def orangecap(dict1):
    dict2 = {}
    for k1 in dict1:
        for k2 in dict1[k1]:
            dict2[k2] = dict2.get(k2, 0) + dict1[k1][k2]
    player = max(dict2, key=dict2.get)
    return player, dict2[player]

import collections
import itertools  
def counter_to_poly(c):
    p = [(coeff, exp) for exp, coeff in c.items() if coeff != 0]
    # sort by exponents in descending order
    p.sort(key = lambda pair: pair[1], reverse = True)
    return p

def addpoly(p, q):
    r = collections.Counter()

    for coeff, exp in (p + q):
        r[exp] += coeff

    return counter_to_poly(r)
def multpoly(p, q):
    r = collections.Counter()

    for (c1, e1), (c2, e2) in itertools.product(p, q):
        r[e1 + e2] += c1 * c2

    return counter_to_poly(r)
import ast

def todict(inp):
    inp = ast.literal_eval(inp)
    return (inp)

def topairoflists(inp):
    inp = "["+inp+"]"
    inp = ast.literal_eval(inp)
    return (inp[0],inp[1])

fncall = input()
lparen = fncall.find("(")
rparen = fncall.rfind(")")
fname = fncall[:lparen]
farg = fncall[lparen+1:rparen]

if fname == "orangecap":
   arg = todict(farg)
   print(orangecap(arg))
elif fname == "addpoly":
   (arg1,arg2) = topairoflists(farg)
   print(addpoly(arg1,arg2))
elif fname == "multpoly":
   (arg1,arg2) = topairoflists(farg)
   print(multpoly(arg1,arg2))
else:
   print("Function", fname, "unknown")
  
