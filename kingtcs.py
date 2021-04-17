n=int(input())
x,y=0,0
dis=10
c='R'

for i in range(n):
    if c=='R':
        x=x+dis
        c='u'
        dis=dis+10
    
    elif c=='u':
        y=y+dis
        c='l'
        dis=dis+10
    
    elif c=='l':
        x=x-dis
        c='m'
        dis=dis+10

    elif c=='m':
        y=y-dis
        c='n'
        dis=dis+10

    elif c=='n':
        x=x+dis
        c=='0'
        dis=dis+10
print(x,y)