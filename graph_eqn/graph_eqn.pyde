def setup():
    global grid_size
    size(600,601)
    grid_size = 15
    # fullScreen()
    
def grid(grid_size):
    try:
        for i in range(width/grid_size):
            for j in range(height/grid_size):
                rect(grid_size*i,grid_size*j,grid_size,grid_size)
        stroke(0,155)
        strokeWeight(1)
        line(width/2,0,width/2,height)
        line(0,height/2,width,height/2)
        stroke(0)
        strokeWeight(0)
    except ZeroDivisionError as err:
        print(err)
    
def graph():
    strokeWeight(1)
    noFill()
    beginShape()
    try:
        
        for i in range(-width/grid_size,width/grid_size):
            
            # y = -1/log(i+1)
            # y = (sin(i))
            y = -(i**2)
            # y = -(i+sin(i))
            # y = -sin(i)
            x = i
            x=map(x,0,width,0,grid_size*width)
            y=map(y,0,height,0,grid_size*height)
            # fill(0)
            stroke(0)
            curveVertex(x,y)
            ellipse(x,y,2,2)
            
    except ZeroDivisionError as err:
        print(err)
        # pass
    endShape()
    fill(255)
    stroke(0)
    strokeWeight(0)
    
    
def draw():
    grid(grid_size)
    translate(width/2, height/2)
    graph()
    
def mouseWheel(event): 
    global grid_size
    e = event.getCount()
    if grid_size <= 2:
        grid_size = 2
    grid_size -= e*4


# def mouseDragged():
#     translate(mouseX, mouseY)

    
    
            
    
