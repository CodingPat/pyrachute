import pgzrun
import random

WIDTH=800
HEIGHT=600
DELAY=3
SPEEDPARACHUTE=5
SPEEDBATEAU=4
MARGEHAUT=50
MARGEBAS=150
WIDTHPARACHUTE=200

def create_parachute():
    parachute=Actor('parachute75px',anchor=('left','bottom'))
    parachute.pos=(random.randrange(0,WIDTH-WIDTHPARACHUTE,50),0)
    parachutes.append(parachute)

    

def update():
    global score
    for index,parachute in enumerate(parachutes):
        parachute.y+=SPEEDPARACHUTE
        if parachute.colliderect(bateau):
            score+=1
            parachutes.pop(index)
        elif parachute.bottom==HEIGHT-MARGEBAS:
            parachutes.pop(index)

    

    if keyboard.left:
        bateau.image='boatleft200px'
        bateau.x-=SPEEDPARACHUTE
    elif keyboard.right:
        bateau.image='boatright200px'
        bateau.x+=SPEEDPARACHUTE
        
    if bateau.left<0:
        bateau.left=0
    elif bateau.right>WIDTH:
        bateau.right=WIDTH

    
        
def draw():
    beach.draw()
    bateau.draw()
    for parachute in parachutes:
        parachute.draw()
    screen.draw.text("Score : {}".format(score),(550,0),fontsize=60)


beach=Actor('beach800px',anchor=('center','bottom'))
bateau=Actor('boatright200px')
bateau.pos=(WIDTH/2,HEIGHT-150)

parachutes=[]

score=0

clock.schedule_interval(create_parachute,DELAY)



pgzrun.go()
