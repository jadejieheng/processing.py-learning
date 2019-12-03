x = 20

angle = 0   
def setup():
    size(1000, 1000)
    strokeWeight(4)
    textSize(100)

def draw():
    global x
    background(204)
    if ((keyPressed) and (key == 'A')):  # If the key is pressed
        x += 1   # add 1 to x 
        line(x, 200, 200-x, 800)
    else:
        rect(400,400,200,200)
    
    text(key,200,200)
    
    if ((keyPressed) and ((key == 'a') or (key == 'A'))):
        line(50, 25, 50, 75)
    else:  
        ellipse(50, 50, 50, 50)
        
    if (keyPressed):
        x = ord(key) + 130
        line(x, 0, x, height)
        #32-126 is value range of the printable (0-31, 127 nonprintable)
        #control characters, normally on the keyboard
    
    global angle
    if (keyPressed):
        if ((ord(key) >= 32) and (ord(key) <= 126)):
            # If the key is alphanumeric, use its value as an angle
            angle = (ord(key) - 32)*4

    arc(150, 150, 66, 66, 0, radians(angle))

    arc(250, 55, 50, 50, 0, HALF_PI, OPEN)
    arc(370, 55, 60, 60, HALF_PI, PI, CHORD)
    arc(450, 55, 70, 70, 0, PI+QUARTER_PI, PIE)
    arc(550, 55, 80, 80, PI+QUARTER_PI, TWO_PI)
    
