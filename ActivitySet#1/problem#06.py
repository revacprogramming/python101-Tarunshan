largest = None
smallest = None
while True:
    num = input("Enter a number: ")
    if num == "done":
        break
    print(num)
    num=int(num)
    l=[]
    l.append(num)
    i=0
    largest=l[i]
    smallest=l[i]
    for i in l:
        if l[i]>largest:
            largest=l[i]
        if l[i]<smallest:
            smallest=l[i]
print("Maximum", largest)
print("Minimum",smallest)