def convert_seconds(x):
    L=[]
    a=x//3600
    b=(x-a*3600)//60
    c=(x-a*3600-b*60)
    
    if a==float(a) and b==float(b):
        a=int(a)
        b=int(b)
    
    A=str(a)+" hours"
    B=str(b)+" minutes"
    C=str(c)+" seconds"
    
    if a==1:
        A="1 hour"
    if b==1:
        B="1 minute"
    if c==1:
        C="1 second"
    
    L.append(A)
    L.append(B)
    L.append(C)    
   
    return L[0]+", "+L[1]+", "+L[2]

print convert_seconds(3661)

print convert_seconds(7325)

print convert_seconds(7261.7)
