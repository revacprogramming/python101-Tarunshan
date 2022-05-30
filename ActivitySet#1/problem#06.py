largest = 0
smallest = 9999

while True:
  num = input("Enter a number: ")
  if num == "done":
      break
  try:
    num=int(num)
    print(num)
    if num>largest:
      largest=num
    if num<smallest:
      smallest=num
    
  except:
    print("Invalid input")
print("Maximum", largest)
print("Minimum",smallest)