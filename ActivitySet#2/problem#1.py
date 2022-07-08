def add(a, b):
  sum=a+b
  return sum


def main():
  a = int(input("Enter number"))
  b = int(input("Enter number"))
  c = add(a, b)
  print("The sum of",a,"and",b,"is",c)

main()
