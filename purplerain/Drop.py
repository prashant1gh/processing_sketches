class Drop:
    def __init__(self, x, y):
        self.x = random(width)
        self.y = random(-500,-20)
        self.z = random(0,20)
        self.le = map(self.z,0,20,10,20)
        self.yspeed = map(self.z, 0, 20, 1, 20)
        

    
    def fall(self):
        self.y = self.y + self.yspeed
        self.grav = map(self.z, 0, 20, 0, 0.2)
        self.yspeed += self.grav
        
        if self.y > height:
            self.y = random(-500,-20)
            self.yspeed = map(self.z, 0, 20, 4, 10)
        
    def show(self):
        self.thick = map(self.z, 0, 20, 1, 2)
        strokeWeight(self.thick)
        stroke('#0f52ba')
        line(self.x,self.y, self.x, self.y+self.le)
        
