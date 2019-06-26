a=input()
s=0
c=0
for i in a:
    if s==0:
        if i=='}':
            c+=1
            s+=1
        else:
            s+=1
    else:
        if i=='{':
            s+=1
        else:
            s-=1
if s!=0:
    d=s//2
print(c+d)
