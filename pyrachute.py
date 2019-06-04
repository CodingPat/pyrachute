import pgzrun
import random
import pygame

WIDTH=800
HEIGHT=600


MAXPARACHUTES=5
SPEEDBATEAU=4
MARGEHAUT=50
MARGEBAS=150
WIDTHPARACHUTE=200



def init():
    global score,delai,delaimax
    bateau.pos=(WIDTH/2,HEIGHT-150)
    parachutes.clear()
    gameover=False
    attentedemarrage=True
    jeuencours=False
    delai=0
    score=0

    
    
def create_parachute():
    global decompteparachutes,vitesseparachute
    
    parachute=Actor('parachute75px',anchor=('left','bottom'))
    parachute.pos=(random.randrange(0,WIDTH-WIDTHPARACHUTE,50),0)
    parachutes.append(parachute)
    decompteparachutes+=1
    if decompteparachutes>=MAXPARACHUTES:
        vitesseparachute+=vitesseplusparachute
        
    
    
    

def update():
    global score,attentedemarrage,jeuencours,gameover,delai
    
    
            

    if jeuencours:
        for index,parachute in enumerate(parachutes):
            parachute.y+=vitesseparachute
            if parachute.colliderect(bateau):
                score+=1
                parachutes.pop(index)
            elif parachute.bottom==HEIGHT-MARGEBAS:
                parachutes.pop(index)
                jeuencours=False
                gameover=True
                

        if keyboard.left:
            bateau.image='boatleft200px'
            bateau.x-=vitesseparachute
        elif keyboard.right:
            bateau.image='boatright200px'
            bateau.x+=vitesseparachute
            
        if bateau.left<0:
            bateau.left=0
        elif bateau.right>WIDTH:
            bateau.right=WIDTH


        delai+=horloge.tick()
        if delai>=delaimax:
            delai=0
            create_parachute()
        

    
     

        

    
        
def draw():

    
    if jeuencours:
        beach.draw()
        bateau.draw()
        for parachute in parachutes:
            parachute.draw()
        screen.draw.text("Score : {}".format(score),(550,0),fontsize=60)

    elif attentedemarrage:
        beach.draw()
        screen.draw.text("Pyrachute (SPACE pour démarrer)",centery=HEIGHT/2,centerx=WIDTH/2, color='red',fontsize=60)

    elif gameover:
        screen.draw.text("Gameover (SPACE pour continuer)",centery=HEIGHT/2,centerx=WIDTH/2, color='red',fontsize=60)


def on_key_up(key):
    
    global attentedemarrage,gameover,jeuencours
    
    if attentedemarrage:
        if key==keys.SPACE:
            attentedemarrage=False
            init()
            jeuencours=True
        
            
    if gameover:
        if key==keys.SPACE:
            gameover=False
            attentedemarrage=True 
    





beach=Actor('beach800px',anchor=('center','bottom'))
bateau=Actor('boatright200px')


parachutes=[]
vitesseparachute=5
vitesseplusparachute=1

score=0
gameover=False
attentedemarrage=True
jeuencours=False

horloge=pygame.time.Clock()
delai=0
delaimax=2000 #millisecondes
decompteparachutes=0

init()


pgzrun.go()
