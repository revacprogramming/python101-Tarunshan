fname = input("Enter file name: ")
fh = open(fname)
lst = list()
for line in fh:
    l=line.split()
    for i in l:
        if i not in lst:
            lst.append(i)
lst.sort()
print(lst)

