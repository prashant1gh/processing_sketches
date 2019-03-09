from Drop import Drop

drops = []

def setup():
    size(1000,700)
    fullScreen()
    for i in range(300):
        drops.append(Drop(random(width), random(0, height-300)))
    

def draw():
    background(0)
    # background(230,230,250)
    for drop in drops:
        drop.fall()
        drop.show()
