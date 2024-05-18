# init  
class Person:
  def __init__(self, name, age, email):
    self.name = name
    self.age = age
    self.email = email

p1 = Person("John", 36, "paul.fatoki.itb@gmail.com")

print(p1.name)
print(p1.age)
print(p1.email)