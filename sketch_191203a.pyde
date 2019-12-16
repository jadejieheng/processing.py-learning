""" pusedocode

c = color(0)
x = 0.0
y = 100.0
speed = 1.0

def setup():
  size(500, 500)

def draw():
  background(255)
  move()
  display()

def move():
  global x
  x = x + speed
  if x > width:
          x = 0

def display():
  fill(c)
  rect(x, y, 150, 50)
  """

""" rewrite the structure, object oriented 

class Car(object):#class name, data(global variables)
    
    def __init__(self):      #initializing data
        self.c = color(255)
        self.x = 100
        self.y = 100
        self.xspeed = 1
    
    def display(self):       #functionality
        rectMode(CENTER)
        fill(self.c)
        rect(self.x, self.y, 100, 50)
    
    def drive(self):         #functionality
        self.x += self.xspeed
        if self.x > width:
            self.x = 0

Note that the code for a class exists as its own block 
and can be placed anywhere outside of setup() and draw(), 
as long as it's defined before you use it.

myCar = Car() #drive() must be called with Car instance as first argument
              #Car is a class, myCar = Car() is an instance
              #Car.drive() is not an argument

def setup():
    size(1000,1000)

def draw():
    background(255)
    myCar.drive()
    myCar.display()
    
result is one  

"""

"""using the object"""

class Car(object):#class name
    
    def __init__(self, c, x, y, xspeed, yspeed):      #initializing data
        self.c = c
        self.x = x
        self.y = y
        self.xspeed = xspeed
        self.yspeed = yspeed
    
    def display(self):       #functionality
        noStroke()
        rectMode(CENTER)
        fill(self.c)
        rect(self.x, self.y, 200, 100)
    
    def drive(self):         #functionality
        
        self.x += self.xspeed
        if self.x > width:   #this loop runs for +speed
            self.x = 0
        if self.x < 0:       #this loop runs for -speed
            self.x = width
        
        self.y += self.yspeed# this has no loop

#myCar = Car()           #initializing an object/object instantiation

#object instantiation
myCar1 = Car(color(204,14,66), 1000, 650, -5, 0) 
myCar2 = Car(color(33,45,201), 0, 350, 2, 0)   
myCar3 = Car(color(234,164,0), 500, 0, 0, 2)

def setup():
    size(1000,1000)

def draw():
    background(255)
    myCar1.drive()       # Functions are called with the "dot syntax".
    myCar1.display()
    myCar2.drive()       
    myCar2.display()
    myCar3.drive()
    myCar3.display()
    

    
    
