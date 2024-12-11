#sum of all even number in a range
start = int(input("enter starting number:"))
end = int(input("enter ending number:"))
even_sum = 0
for i in range(start,end+1):
  if i % 2 == 0:
    even_sum += i
print("sum of even number is :",even_sum)
