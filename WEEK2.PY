def intreverse(n):
    return int(str(n)[::-1])

    

def matched(str):
    x = 0
    y = 0
    for i in range(0,len(str)):
        l = str[i]
        if l == "(":
            x = x+1
        else:
            if l == ")" and x>y:
                y = y + 1
            elif l == ")" and x <= y:
                return False
    if x==y:
        return True
    else:
        return False
      
      
def isprime(n):
    
    if n==1 or n < 0:
        return False
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False

    return True


def sumprimes(l):
    x = len(l)
    s = 0
    for i in range(0,x):
        if isprime(l[i]):
            s = s + l[i]

    return (s)
import ast

def tolist(inp):
  inp = "["+inp+"]"
  inp = ast.literal_eval(inp)
  return (inp[0],inp[1])

def parse(inp):
  inp = ast.literal_eval(inp)
  return (inp)

fncall = input()
lparen = fncall.find("(")
rparen = fncall.rfind(")")
fname = fncall[:lparen]
farg = fncall[lparen+1:rparen]

if fname == "intreverse":
   arg = parse(farg)
   print(intreverse(arg))
elif fname == "matched":
   arg = parse(farg)
   print(matched(arg))
elif fname == "sumprimes":
   arg = parse(farg)
   print(sumprimes(arg))
else:
   print("Function", fname, "unknown")

