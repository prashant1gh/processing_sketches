from ball import Ball
ballList = []

num_particle = 50
def setup():
    global  num_particle
    fullScreen()
    size(600,600)
    for i in range(num_particle):
        ballList.append(Ball(random(width), random(height)))
        
def keyPressed():
    global  num_particle
    
        
        
    if num_particle>10:
        if key == 'a':
            num_particle+=10
            for i in range(10):
                ballList.append(Ball(random(width), random(height)))
        elif key == 's':
            num_particle-=10
            for i in range(10):
                ballList.pop()


    
def draw():
    background(0)
    for ball in ballList:
        ball.update()
        ball.check(ballList)
        md = dist(mouseX,mouseY,ball.xcor,ball.ycor)
        if md < 150:
            stroke(8, 146, 208,map(md,0,150,0,250))
            line(mouseX, mouseY,ball.xcor,ball.ycor)
