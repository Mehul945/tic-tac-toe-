# from pytube import YouTube
# a=input("enter link : ")
# reso = input("enter reso : ")
# yt = YouTube(a)
# print(yt.streams)
# t = yt.streams.filter(progressive="True", res=reso)
# for i in range(len(t)):
    # print(t[i])
    # print("<<<< START DOWNLODING >>>>")
    # t.first().download()
    # print("<<<< FINISED >>>>")
# print(random.randint(1,100))
a="""
   |   |   
___|___|___
   |   |   
___|___|___
   |   |   
   |   |   """
print(a,end="")
# 1,5,9,23,27,31,46,50,54
b=list(a)
p1l=[]
def p1m(p1):
    if p1==1:
        b[1]="X"
        for i in b:
            print(i,end="")
    elif p1==2:
        b[6]="X"
        for i in b:
            print(i,end="")
    elif p1==3:
        b[10]="X"
        for i in b:
            print(i,end="")
    elif p1==4:
        b[25]="X"
        for i in b:
            print(i,end="")
    elif p1==5:
        b[30]="X"
        for i in b:
            print(i,end="")
    elif p1==6:
        b[34]="X"
        for i in b:
            print(i,end="")
    elif p1==7:
        b[49]="X"
        for i in b:
            print(i,end="")
    elif p1==8:
        b[54]="X"
        for i in b:
            print(i,end="")
    elif p1==9:
        b[58]="X"
        for i in b:
            print(i,end="")
    return p1

def p2m(p2):
    if p2==1:
        b[1]="O"
        for i in b:
            print(i,end="")
    elif p2==2:
        b[6]="O"
        for i in b:
            print(i,end="")
    elif p2==3:
        b[10]="O"
        for i in b:
            print(i,end="")
    elif p2==4:
        b[25]="O"
        for i in b:
            print(i,end="")
    elif p2==5:
        b[30]="O"
        for i in b:
            print(i,end="")
    elif p2==6:
        b[34]="O"
        for i in b:
            print(i,end="")
    elif p2==7:
        b[49]="O"
        for i in b:
            print(i,end="")
    elif p2==8:
        b[54]="O"
        for i in b:
            print(i,end="")
    elif p2==9:
        b[58]="O"
        for i in b:
            print(i,end="")
    return p2
            
def pw():
    if b[1]==b[6]==b[10]=="X" or b[25]==b[30]==b[34]=="X" or b[49]==b[54]==b[58]=="X" or b[1]==b[25]==b[49]=="X" or b[6]==b[30]==b[54]=="X" or b[10]==b[58]==b[34]=="X" or b[10]==b[30]==b[49]=="X" or b[1]==b[30]==b[58]=="X":
        print("Player 1 winner")
        return 1
    elif b[1]==b[6]==b[10]=="O" or b[25]==b[30]==b[34]=="O" or b[49]==b[54]==b[58]=="O" or b[1]==b[25]==b[49]=="O" or b[6]==b[30]==b[54]=="O" or b[10]==b[58]==b[34]=="O" or b[10]==b[30]==b[49]=="O" or b[1]==b[30]==b[58]=="O":
        print("player 2 winner")
        return 1
    else:
        return 0
p1l=[0]
p2l=[0]
def chackVailidMove1(y):
    p1=int(input("player 1 : Enter input : "))
    p1l.append(p1)
    p1s=set(p1l)
    if p1 in y:
        print("Invalid entry")
        chackVailidMove1(y)
    else:
        p1m(p1)
    return p1s
def chackVailidMove2(y):
    p2=int(input("player 2 : Enter input : "))
    p2l.append(p2)
    p2s=set(p2l)
    if p2 in y:
        print("Invalid entry")
        # p2m(p2)
        chackVailidMove2(y)
    else:
        p2m(p2)
    return p2s
def chack():
    if not(b[1]==" " or b[6]==" " or b[10]==" " or b[25]==" " or b[30]==" " or b[34]==" " or b[49]==" " or b[54]==" " or b[58]==" "):
        print("\nGame Draw\n")
        return 1
while 1:
    q=set(p1l)
    p=set(p2l)
    q=q.union(p)
    chackVailidMove1(q)
    q=set(p1l)
    p=set(p2l)
    q=q.union(p)
    p=q
    p1w1=pw()
    if p1w1==1:
        break
    ch=chack()
    if ch==1:
        break
    chackVailidMove2(q)
    p1w1=pw()
    if p1w1==1:
        break