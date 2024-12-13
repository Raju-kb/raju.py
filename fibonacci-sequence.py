#fibonacci sequece
n =int(input("enter the number of terms:"))
a,b = 0,1
for  i in range(n):
  print(a)
  a,b = b,a+b
