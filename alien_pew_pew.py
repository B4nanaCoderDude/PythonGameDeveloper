import pgzrun
import random
HEIGHT=600
WIDTH=600
TITLE="Alien pew-pew"
message=""
score=0
alien=Actor("alienimage")
alien.pos=300,300
def draw():
    screen.clear()
    screen.fill(color=(255,40,40))
    alien.draw()
    screen.draw.text(message,(100,100),fontsize=30)
    screen.draw.text("score= "+str(score),(350,100),fontsize=25)
def alienplace():
    alien.x=random.randint(50,550)
    alien.y=random.randint(50,500)
def on_mouse_down(pos):
    global message
    global score
    if alien.collidepoint(pos):
        message="You hit the alien!"
        alienplace()
        score=score+1
    else:
        message="You missed the alien."
        score=score-1
alienplace()
pgzrun.go()