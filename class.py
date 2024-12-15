class person:
  def __init__(self,name,age):
    self.name = name
    self._age = age
    self.__salary = 5000

  def get_salary(self):
    return self.__salary

  def set_salary(self,new_salary):
    if new_salary > 0:
      self.__salary = new_salary
    else:
      print("salary must be positive")
  def display_info(self):
    print(f"name:{self.name},age :{self._age},salary:{self.__salary}")

person1 = person("alice",25)
person1.display_info()
person1.set_salary(6000)
person1.display_info()
