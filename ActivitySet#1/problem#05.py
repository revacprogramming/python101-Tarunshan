def computepay(h, r):
    if h>40:
        p1=40*r
        r=r*1.5
        p2=(h-40)*r
        pay=(p1+p2)
    else:
        pay=h*r
    return pay
hrs=float(input("Enter Hours:"))
r=float(input("Enter rate"))
p = computepay(hrs,r)
print("Pay", p)
