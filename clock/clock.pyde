
def setup(): 
    global font
    # fullScreen()
    size(600,600)
    font = createFont("Radioland", 45)
    textFont(font, 32)

def draw(): 
    background(0)
    s = second()
    m = minute() 
    h = hour()
    fill(8,146,208)
    string = str(h)+' : ' +str(m)+ ' : ' +str(s)
    textFont(font)
    text(string,width/2-100,height/2)

    
