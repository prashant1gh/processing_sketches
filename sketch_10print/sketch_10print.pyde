x,y = 0,0
spacing = 30

def setup():
    size(800,800)
    background(0)
    
def draw():
    global x, y
    stroke('#7ef9ff')
    if random(1)<0.5:
        line(x, y, x+spacing, y+spacing)
    else:
        line(x, y+spacing, x+spacing, y)
    x += spacing
    if x >= width:
        x = 0
        y+=spacing
