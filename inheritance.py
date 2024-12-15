class parentclass:
  def __init__(self, name):
    self.name = name
  def greet(self):
    print(f"hello,{self.name}")
class childclass(parentclass):
  def __init__(self, name, age):
    super().__init__(name)
    self.age = age
  def age1(self):
    print(f"{self.age}years old")

child = childclass("alice",25)
child.greet()
child.age1()
