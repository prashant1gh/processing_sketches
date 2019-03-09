

def setup():
    global font
    size(600,600)
    font = createFont("Radioland", 45)
    textFont(font)
    
def draw():
    sec=second()    
    hou = map(hour(),0,24,0,12)    
    mi = minute()
    ms = millis()
    
    background(0)
    noFill()
    stroke(255)
    strokeWeight(3)
    translate(width/2, height/2)
    string = str(hour())+' : ' +str(mi)+ ' : ' +str(sec)
    textFont(font)
    textSize(15)
    text(string,0-50,0)
    rotate(radians(-90))
    # ellipse(0, 0,150,150)
    stroke(8, 146, 208)
    strokeWeight(5)

   
    stroke(255,255,255,15)
    ellipse(0,0,250,250)
    stroke(8, 146, 208)
    arc(0, 0, 250, 250, 0, map(sec,0,60,0,TWO_PI))
    
    stroke(255,255,255,15)
    ellipse(0,0,350,350)
    stroke(8, 146, 208)
    arc(0, 0, 350, 350, 0, map(mi,0,60,0,TWO_PI))
    
    stroke(255,255,255,15)
    ellipse(0,0,450,450)
    stroke(8, 146, 208)
    arc(0, 0, 450, 450, 0, map(hou,0,24,0,TWO_PI))

    



    
    
