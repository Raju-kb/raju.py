def fibonacci(n):
  sequence = []
  a,b = 0,1
  for i in range(n):
    sequence.append(a)
    a,b = b,a+b
  return sequence
num_terms = int(input("enter the number of terms :"))
fib_sequence = fibonacci(num_terms)
print("fibonacci sequence :",fibonacci(num_terms))
