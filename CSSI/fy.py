'''
class MyClass:
  """example class"""
  def __init__(self):
    self.name = 'Brooklyn NY'


  def getName(self):
    return 'hello ' + self.name


myObject=MyClass()
print myObject.getName()

class MyClass:
  """example class"""
  def __init__(self, my_name):
    self.name = my_name


  def getName(self):
    return 'hello ' + self.name

M1 = MyClass("foo")
M2 = MyClass("bar")

print M1.getName()
print M2.getName()
'''
'''
class Spaceship:
    def __init__ (self, Spaceship_name, Spaceship_color, Spaceship_speed):
        self.name = Spaceship_name
        self.color = Spaceship_color
        self.speed = Spaceship_speed

    def description(self):
        print "Hey, my Spaceship name is %s and color id %s and speed is %s Spaceship." % (self.name, self.color,self.speed)

move = Spaceship('gib', 'blue', 450)
ride = Spaceship('Mozart', 'pink', 549)

print (move.name + ': ' + move.color)
print (ride.name + ': ' + str(ride.speed))

ride.description()
'''
class Box:
    def __init__(self, width,height, border):
        self.width = Box.width
        self.height = Box.height
        self.border = Box.border

    def getWidth(self):
        return width
