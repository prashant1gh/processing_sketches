


def setup():
    global xpos, ypos, xspeed
    fullScreen()
    size(600,600)
    xpos = width
    ypos = height/2
    xspeed = 8
    
def draw():
    global xpos, ypos, xspeed
    background(0)

    textSize(300)
    text("KONICA", xpos, ypos)
    
    xpos -= xspeed
    
    if xpos < -1100:
        xpos = width
        fill(random(255),random(255),random(255))
