import pgzrun
HEIGHT=500
WIDTH=500
def draw():
    screen.draw.filled_circle((250,300),75,"white")
    screen.draw.filled_circle((250,180),50,"white")
    screen.draw.filled_circle((230,160),10,"dark grey")
    screen.draw.filled_circle((275,155),10,"black")
    screen.draw.filled_circle((250,260),5,"black")
    screen.draw.filled_circle((250,295),5,"black")
    screen.draw.filled_circle((253,325),6,"black")
    screen.draw.line((325,300),(375,275),"brown")
    screen.draw.line((175,300),(125,280),"brown")
    screen.draw.text("This is Bob XXVI the snowman. Say hi!",(100,100),color="white",fontsize=20)
    screen.draw.line((250,180),(275,190),"orange")
    screen.draw.line((275,190),(250,200),"orange")
    screen.draw.line((250,200),(250,180),"orange")
pgzrun.go()