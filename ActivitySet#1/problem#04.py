hrs = input("Enter Hours:")
h = float(hrs)
r=float(input("Enter rate"))
if h>40:
    p1=40*r
    r=r*1.5
    p2=(h-40)*r
    print(p1+p2)
else:
    print(h*r)
    