from star import Star
speed = 0
starList = []

def setup():
    size(800,800)
    fullScreen()
    for i in range(4000):
        starList.append(Star())
    
def draw():
    background(0)
    translate(width/2, height/2)
    for star in starList:
        star.update()
        star.show()
