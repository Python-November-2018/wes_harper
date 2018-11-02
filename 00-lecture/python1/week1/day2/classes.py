class Human:
  def __init__(self, eye_col, name):
    self.eye_color = eye_col
    self.name = name
    self.health = 100

  def say_name(self):
    print("Hi, my name is " + self.name)
    return self

  def workout(self):
    self.health += 10
    return self
  
  def display_health(self):
    print(self.health)
    return self

class Nerd(Human):
  def __init__(self, eye_col, name, favorite_book):
    super().__init__(eye_col, name)
    self.favorite_book = favorite_book

  def read(self):
    print("Deep in thought...")
    return self

wes = Nerd("blue", "Wes", "Hitchhiker's Guide")
jay = Human('brown', "Jay")

print(wes.favorite_book)
# print(wes.say_name())

wes.workout().display_health().workout().display_health().read()
jay.workout().display_health()

# return statements
  # ends/leaves the function
  # returns the value where it was called
  # continues execution at the place where it was called