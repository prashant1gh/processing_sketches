class Ball:
    def __init__(self, x, y):
        self.xcor = x
        self.ycor = y
        self.xvel = random(-0.3,0.5)
        self.yvel = random(-0.8,0.9)
        self.col = color(255)#color(random(255), random(255), random(255))  
        self.si = 5
          
        
    def update(self):
        self.xcor += self.xvel
        self.ycor += self.yvel
        
        if self.xcor>width or self.xcor<0:
            self.xvel = -self.xvel
        if self.ycor>height or self.ycor<0:
            self.yvel = -self.yvel
        fill(self.col)
        ellipse(self.xcor, self.ycor, self.si,self.si)
    
    def check(self, l):
        for Ball in l:
            d = dist(Ball.xcor,Ball.ycor,self.xcor,self.ycor) 
             
            self.col=(map(d,0,width,10,250))
            if d < 150:
                stroke(8, 146, 208,map(d,0,150,0,50))
                line(Ball.xcor,Ball.ycor,self.xcor,self.ycor)          
                
