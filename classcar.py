class car:
  no_of_seat = 4
  milage = 70
  no_of_wheels = 4

  def moveforward(self):
    print("car is moving forward:")
  def movebackward(self):
    print("car is turning backward:")
  def turnleft(self):
    print("car is moving forward:")
  def turnright(self):
    print("car is moving forward:")

car1 = car()
car1.moveforward()
car1.movebackward()
car1.turnleft()
car1.turnright()



car2 = car()
print(car2.no_of_wheels)
print(car2.no_of_seat)
print(car2.milage)


car3 = car()
car3.milage =100
car3.no_of_seat = 5
car3.no_of_wheels =6
print(car3.milage)
print(car3.no_of_wheels)
print(car3.no_of_seat)
print(car3.milage)
