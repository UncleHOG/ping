ellx=250
elly=400
speedx=0
speedy=0
rackl=360
rackr=360
n=0
l1=10
l2=10
l3=10
m=0

def setup():
    size(500,600)
def draw():
    global ellx,elly,speedx,speedy,rackl,rackr,n,l1,l2,l3,m
    fill(0)
    rect(0,0,500,600)
    if m==1:
        l3=-20
    if m==2:
        l2=-20
    if m==3:
        l1=-20
    if elly>=570:
       #speedy=speedy+1 
       speedy=-speedy
    if ellx>=500:
       speedx=0
       speedy=0
       ellx=250
       elly=400
       n=0       
    if elly<=230:
       speedy=-speedy
    if ellx<=0:
       speedx=0
       speedy=0
       ellx=250
       elly=400
       n=0
       m=m+1
    fill(0,255,0);
    rect(20,220,460,360)
    ellipse(10,l1,10,10)
    ellipse(20,l2,10,10)
    ellipse(30,l3,10,10)
    line(20,400,480,400)                            #gorizontalnaya poloska na pole
    line(250,230,250,570)
    fill(0,0,255);   
    rect(20,rackl,10,80)                            #racketki
    rect(470,rackr,10,80)
    fill(255,0,255)
    triangle(245,220,255,220,250,230)
    triangle(245,580,255,580,250,570)
    fill(255,0,0)
    ellipse(ellx,elly,10,10)
    ellx=ellx+speedx
    elly=elly+speedy
    if keyPressed:
        if key == 'p' and n == 0:
            speedy -= 2
            speedx -= 2
            n += 1
        if key == 'w' and rackl>=222:
            rackl=rackl-2
        if key == 's' and rackl<=498: 
            rackl=rackl+2
        if key == 'o' and rackr>=222:
            rackr=rackr-2
        if key == 'l' and rackr<=498:
            rackr=rackr+2    

    
    if ellx <=35 and elly >= rackl and elly <= rackl+80:
        speedx=-speedx
             

     
