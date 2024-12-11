#largest of 3 numbers
num1 = float(input("enter first number:"))
num2 = float(input("enter second number:"))
num3 = float(input("enter third number:"))
if num1>=num2 and num1>=num3:
  print("largest number is :",num1)
elif num2>=num3:
  print("largest number  is :",num2)
else:
  print("largest number is :",num3)
