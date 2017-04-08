ballx=100
bally=100
xspeed=1
yspeed=1
racketl=100

def setup():
    size(600,400)
   
    
def draw():
    global ballx,bally,xspeed,yspeed,racketl
    rect(20,20,560,360)
    rect(20,racketl,10,150)
    rect(570,100,10,150)
    ellipse(ballx,bally,5,5)
    ballx=ballx+xspeed
    bally=bally+yspeed
    if keyPressed:
        if key == 'w' and racketl>=22:
            racketl=racketl-2
        if key == 's' and racketl<=228:
            racketl=racketl+2
 
    if bally>=375:
        yspeed=yspeed+1
        yspeed=-yspeed
    if ballx>=575:
        xspeed=-xspeed
    if bally<=25:
        yspeed=-yspeed
    if ballx<=25:
        xspeed=-xspeed
