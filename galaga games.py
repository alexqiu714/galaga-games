import pgzrun
from time import time

WIDTH = 700
HEIGHT = 700

bugs = []
Bullet = []
bugstoremove = []
bulletstoremove = []

a = Actor("galaga")
a.x = 250
a.y = 567
score = 0
direction = 1
movedown = False
youwin = False
gameover = False
Time = time()

for n in range(4):
    for i in range(4):
        b = Actor("bug")
        b.x = (i * 85) + 220
        b.y = (n * 67) + 60
        bugs.append(b)

def update():
    global movedown, direction, score
    movedown = False
    if keyboard.left:
        a.x = a.x - 5
        if a.x <= 0:
            a.x = 0
    if keyboard.right:
        a.x = a.x + 5
        if a.x >= 700:
            a.x = 700
    for i in Bullet:
        i.y -= 5
        for b in bugs:
            if b.colliderect(i):
                bulletstoremove.append(i)
                bugstoremove.append(b)
                score += 1
    for i in bulletstoremove:
        if i in Bullet:
            Bullet.remove(i)
    for i in bugstoremove:
        if i in bugs:
            bugs.remove(i)
    if len(bugs) > 0 and (bugs[-1].x >= 700 or bugs[0].x <= 0):
        movedown = True
        direction = direction * -1
    if len(bugs) == 0:
        win()
    for i in bugs:
        i.x += 3 * direction
        if movedown == True:
            i.y += 50

def on_key_down(key):
    if key == keys.SPACE:
        bullet = Actor("bullet")
        Bullet.append(bullet)
        bullet.x = a.x
        bullet.y = a.y - 20

def draw():
    screen.fill("light blue")
    a.draw()
    for i in bugs:
        i.draw()
    screen.draw.text("Score: " + str (score), (315,20))
    for i in Bullet:
        i.draw()
    if youwin == True:
        win()
    if gameover == True:
        screen.fill("light blue")
        screen.draw.text("Time's up, you lose", (300, 300))
    total = time() - Time
    screen.draw.text(str (total), (40,40))
 
def win():
    global youwin
    youwin = True
    screen.fill("light blue")
    screen.draw.text("You win!", (320,320))

def time_up():
    global gameover
    gameover = True


clock.schedule(time_up, 10.0)

pgzrun.go()