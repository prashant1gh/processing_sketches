total = 100

def setup():
    global r, factor
    # fullScreen()
    size(600,600)
    factor = 1
    r = width/2
    # frameRate(1)
    
def getVector(index, total):
    angle = map(index % total, 0, total, 0, TWO_PI)    
    v = PVector.fromAngle(angle-PI)
    v.mult(r)
    return v

def draw():
    global factor
    total = int(map(mouseY, 0, height, 0, 200))
    # factor += 0.01
    factor += map(mouseX,0,width,0,0.1)
    background(0)
    translate(width/2, height/2)
    stroke(255)
    noFill()
    ellipse(0,0,r*2,r*2)
    for i in range(total):
        v = getVector(i, total)
        fill(255)
        ellipse(v.x,v.y,8,8)
        
    for i in range(total):
        a = getVector(i, total)
        b = getVector(i * factor, total)
        line(a.x,a.y,b.x,b.y)
        
    # saveFrame("output/####.png")
