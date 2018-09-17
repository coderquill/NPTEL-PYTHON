def stu_input(l):
    x=input()
    while x!='Grades':
        x=x.split('~')
        x.append(0)
        l.append(x)
        x=input()

def inp_grade(grade) :
    x=input()
    while x!='EndOfInput' :
        x=x.split('~')
        x=x[len(x)-2:]
        grade.append(x)
        x=input()
def com(x):
    if x=='A':
        return 10
    elif x=='AB':
        return 9
    elif x=='B':
        return 8    
    elif x=='BC':
        return 7
    elif x=='C':
        return 6
    elif x=='CD':
        return 5
    else:
        return 4
def cal():
    global li,grade
    for i in li:
        j=0
        sum=0
        while j<len(grade):
            if i[0]==grade[j][0]:
                sum=sum+com(grade[j][1])
                grade.pop(j)
                i[2]+=1
            else :
                j+=1
        if sum!=0 :
            i[2]=round(sum/i[2],2)
        print(i[0]+'~'+i[1]+'~',i[2],sep='')
    
li=[]
grade=[]
x=input()
while x!='Students':
    x=input()
stu_input(li)   
li.sort()
inp_grade(grade)
cal()
