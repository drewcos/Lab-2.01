#float('1')
#str(1+'2')
#str('2')
a=input("Enter a number: ")
print(int(a)/2)
print(int(int(a)/2))

m=input("Integer or Float mode? ")

if m == "I":
  print(int(int(a)/2))
else:
  print(float(a)/2)