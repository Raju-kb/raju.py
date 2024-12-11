number = int(input("enter a number:"))
if number % 5 == 0 and number % 10 != 0:
  print(f"{number } is divisible by 5 but not 10")
else:
  print(f"{number } does not satisfy the condition")
