frame = 0

def setup():
    size(1000, 1000)
    #noLoop()
    noCursor()

def draw():
    background(204)
    line(mouseX, 0, mouseX, width)
    line(0, mouseY, height, mouseY)
    #ellipse(mouseX, mouseY, 20, 20)
    if (mousePressed):
        cursor(HAND)
    else:
        cursor(CROSS)
    """
    global frame
    if (frame > 120):   # If 120 frames since the mouse
        noLoop()   # was pressed, stop the program
        background(0)   # and turn the background black.
    else:   # Otherwise, set the background
        background(204)   # to light gray and draw lines
        line(mouseX, 0, mouseX, 1000)   # at the mouse position
        line(0, mouseY, 1000, mouseY)
        frame += 1
    """
def mousePressed():
    """
    global frame
    loop()
    frame = 0
    """
    redraw()
