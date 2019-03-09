xpos, ypos = 300,300
xspeed, yspeed = 5,8




def setup():
    global dvd
    fullScreen()
    tint(random(256),random(256),random(256))
    dvd = loadImage("dvd_logo.png")
    size(1000,800)

    
def draw():
    global xpos, ypos, xspeed, yspeed
    background(0)
    
    image(dvd,xpos,ypos,dvd.width, dvd.height)
    
    xpos += xspeed
    ypos += yspeed
    
    
    if xpos + dvd.width > width or xpos < 0:
        tint(random(100, 256),random(100, 256),random(100, 256))
        xspeed = xspeed * -1
    if ypos + dvd.height > height or ypos < 0:
        tint(random(100, 256),random(100, 256),random(100, 256))
        yspeed = yspeed * -1
    
