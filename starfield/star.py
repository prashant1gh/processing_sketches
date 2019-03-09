class Star:
    def __init__(self):
        self.x = random(-width, width)
        self.y = random(-height, height)
        self.z = random(width)
        
    def update(self):
        self.speed = map(mouseX, 0, width, 0, 20)
        self.z -= self.speed 
        if self.z < 1:
            self.z = width
        
            self.x = random(-width, width)
            self.y = random(-height, height)
        
    def show(self):
        fill(255)
        noStroke()
        self.sx = map(self.x / self.z, 0, 1, 0, width)
        self.sy = map(self.y / self.z, 0, 1, 0, height)
        
        self.r = map(self.z, 0, width, 16, 0)
        ellipse(self.sx,self.sy,self.r, self.r)
        
        
    
