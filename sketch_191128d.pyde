y = 35
R = 0
G = 0
B = 0
drawT = False
drawa = False
drawb = False
drawc = False
drawd = False

def setup():
  size(1000, 1000)
  global f
  f = createFont("Arial",16)

def draw():
    global y
    background(R,G,B)
    stroke(255,200,233)
    line(100, 50, 190, 50)
    if (key == CODED):
        if (keyCode == UP):
            y = 20
        elif (keyCode == DOWN):
            y = 50
    else:
        y = 35
    rect(120, y, 50, 30)
    
    #if (keyPressed):
       # x = ord(key) - 32
        #line(x, 0, x, height)
        #ord and coded key cannot exist together?

    global drawT
    if (drawT):
        noStroke()
        rect(20, 20, 60, 20)
        rect(39, 40, 22, 45)
    global drawa
    if (drawa):
        textFont(f,160)
        text("a",mouseX,200)
    if (drawb):
        textFont(f,160)
        text("b",mouseX + 90,200)
    if (drawc):
        textFont(f,160)
        text("c",mouseX + 180,200)
    if (drawd):
        textFont(f,160)
        text("d",mouseX + 270,200)

def keyPressed():
    global drawT
    if ((key == 'T') or (key == 't')):
        drawT = True
    global drawa
    if (key == 'a'):
        drawa = True    
    global drawb
    if (key == 'b'):
        drawb = True
    global drawc
    if (key == 'c'):
        drawc = True
    global drawd
    if (key == 'd'):
        drawd = True 

def keyReleased():
    global drawT
    drawT = False

def mousePressed():
    global R, B
    R += 5
    B += 20

def mouseReleased():
    global G, B
    G += 10
    B -= 10
    

  
    
