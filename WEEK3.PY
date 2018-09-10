def descending(l) : 
    flag=True
    for i in range (len(l)-1) : 
        if(l[i] < l[i+1]) :
            flag=False
    return flag
  
  
def valley(list):
    if (len(list) < 3):
        return False
    ucount = 1
    lcount = 1
    for i in range(0, len(list) - 1):
        if list[i] > list[i + 1]:
            if lcount > 1:
                return False
            ucount = ucount + 1
        if list[i] < list[i + 1]:
            lcount = lcount + 1
        if list[i] == list[i + 1]:
            return False
    if ucount >1 and lcount > 1:
        return True
    else:
        return False

      
def transpose(matrix):
    matrix = list(map(list, zip(*matrix))) # assign result 
    return matri
import ast

def parse(inp):
  inp = ast.literal_eval(inp)
  return (inp)

fncall = input()
lparen = fncall.find("(")
rparen = fncall.rfind(")")
fname = fncall[:lparen]
farg = fncall[lparen+1:rparen]

if fname == "descending":
  arg = parse(farg)
  print(descending(arg))

if fname == "valley":
  arg = parse(farg)
  print(valley(arg))

if fname == "transpose":
  arg = parse(farg)
  print(transpose(arg))
  


