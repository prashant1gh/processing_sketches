scl = 30
w = 3500
h = 1600

flying = 0

def setup():
    global w,h,flying,rows,cols,terrain
    size(600,600,P3D)
    fullScreen()
    cols = w/scl
    rows = h/scl
    terrain = [['_']*rows for i in range(cols)]

def draw():
    global flying, rows, cols
    flying -= 0.1
    
    yoff = flying
    for y in range(rows):
        xoff = 0.1
        for x in range(cols):
            terrain[x][y] = map(noise(xoff, yoff),0, 1, -70, 90)
            xoff += 0.2
        yoff += 0.2
        
    background(0)
    stroke(8,146,208,100)
    # stroke(0,0,255,150)
    noFill()
    
    translate(width/2, height/2)
    rotateX(PI/2.3)
    translate(-w/2,-h/2)
    
    for y in range(rows-1):
        beginShape(TRIANGLE_STRIP)
        for x in range(cols):
            vertex(x*scl, y*scl, terrain[x][y])
            vertex(x*scl,(y+1)*scl, terrain[x][y+1])
        endShape()
        
