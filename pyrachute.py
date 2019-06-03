import pgzrun
import random

WIDTH=800
HEIGHT=600
DELAY=3
SPEED=5
MARGINTOP=50
WIDTHPARACHUTE=200

def create_parachute():
    parachute=Actor('parachute75px',anchor=('left','bottom'))
    parachute.pos=(random.randrange(0,WIDTH-WIDTHPARACHUTE,50),0)
    parachutes.append(parachute)

    

def update():
    for index,parachute in enumerate(parachutes):
        parachute.y+=SPEED
        if parachute.bottom==0:
            parachutes.pop(index)


def draw():
    beach.draw()
    boat.draw()
    for parachute in parachutes:
        parachute.draw()


beach=Actor('beach800px',anchor=('center','bottom'))
boat=Actor('boat200px')
boat.pos=(WIDTH/2,HEIGHT-150)

parachutes=[]



clock.schedule_interval(create_parachute,DELAY)


pgzrun.go()
