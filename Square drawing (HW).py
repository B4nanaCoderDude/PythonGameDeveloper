import pgzrun
WIDTH=500
HEIGHT=500
def draw():
    screen.clear()
    screen.draw.line((100,100),(100,0),"yellow")
    screen.draw.line((100,0),(0,0),"green")
    screen.draw.line((0,0),(0,100),"red")
    screen.draw.line((0,100),(100,100),"blue")
pgzrun.go()