def setup():
    #this is your canvas size
    size(1000,1000)
    #fill(34,45,56,23)
    #background(192, 64, 0)
    stroke(255)
    colorMode(RGB)
    strokeWeight(1)
    #rect(150,150,150,150)
    
def draw():
    x=mouseX
    y=mouseY
    ix=width-x
    iy=height-y
    px=pmouseX
    py=pmouseY
   
    background(0,0,0)
    #rect(150,150,150,150)
    strokeWeight(5)
    line(x,y,ix,iy)
    #line(x,y,px,py)
    
    strokeWeight(120)
    point(40,x)
    
    if (mousePressed == True):
        if (mouseButton == LEFT):
            fill(196,195,106,255)
            #box(200,500,500)
            strokeWeight(0)
            rectMode(CENTER)
            rect(height/2,width/2,ix,100)
    
    strokeWeight(0)
    fill(144,135,145)
    rectMode(CORNERS)
    rect(mouseX-10,iy-10,width/2,height/2)
   
    fill(155,211,211)
    rectMode(CORNER)
    rect(mouseX,mouseY,50,50)
    
    fill(205,126,145)
    ellipseMode(CORNER)
    ellipse(px,py,35,35)
    #colorMode(RGB,100,100,100,100)
    
    fill(80,98,173,188)
    ellipseMode(CORNERS)
    ellipse(x*.75,y*.75,35,35)
    
    frameRate(12)
    println(str(mouseX)+"."+str(mouseY))
    println(pmouseX-mouseX)
    print("why is it there?")
    
    if (x>500):
        fill(255,160)
        rect(0,0,x,height)
    else:
        fill(255,160)
        rect(0,0,width-ix,height)
    
    if ((x>250) and (x<500) and (y>500) and (y<1000)):
        fill(255)
        rect(250,500,250,500)
        fill(245,147,188)
        rectMode(CORNER)
        rect(mouseX,mouseY,50,50)
    if ((x>0) and (x<250) and (y>500) and (y<1000)):
        fill(255)
        rect(0,500,250,500)
        fill(20,126,145)
        ellipseMode(CORNER)
        ellipse(px,py,35,35)  
    
    if (mousePressed and (x>500)):
        background(255,255,255)
        fill(200)
        rectMode(CENTER)
        rect(width/2,height/2,500,500)
        #colorMode(RGB,100,100,100,100)
        ellipseMode(CORNERS)
        fill(170,170,170,255)
        strokeWeight(4)
        ellipse(width/2-125,height/2-125,width/2-75,height/2-75)
        ellipse(width/2+75,height/2-125,width/2+125,height/2-75)
        
        a = width/2
        b = height/2
        strokeWeight(7)
        noFill()
        curve(a-125,1.4*b-125,a-50,1.4*b-95,a+50,1.4*b-95,a+125,1.4*b-125)
        
    
    

    
