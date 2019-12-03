def setup():
    size(1000, 1000)
    stroke(0)
    background(255)

def draw():
    if (keyPressed):
        x = ord(key) - 32
        line(x, 0, x, height)

   

def draw():
    pass
# pass just tells Python mode to not do anything here, draw() keeps the program running

def mousePressed():
    fill(0, 102)
    rect(mouseX, mouseY, 330, 330)
    # works with no background in draw(), in draw!!!!

moveX = moveY = dragX = dragY = -20

def draw():
    global moveX, moveY, dragX, dragY
    #background(205)
    fill(0)
    ellipse(dragX, dragY, 33, 33)   # Black circle
    fill(153)
    ellipse(moveX, moveY, 33, 33)   # Gray circle

def mouseMoved():  # Move gray circle
    global moveX, moveY
    moveX = mouseX
    moveY = mouseY

def mouseDragged():   # Move black circle
    global dragX, dragY
    dragX = mouseX
    dragY = mouseY
    
