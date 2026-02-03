import pgzrun

WIDTH = 700
HEIGHT = 700

bugs = []

a = Actor("galaga")
a.x = 250
a.y = 567

for n in range(4):
    for i in range(4):
        b = Actor("bug")
        b.x = (i * 85) + 220
        b.y = (n * 67) + 60
        bugs.append(b)

def update():
    if keyboard.left:
        a.x = a.x - 5
        if a.x <= 0:
            a.x = 0
    if keyboard.right:
        a.x = a.x + 5
        if a.x >= 700:
            a.x = 700

def draw():
    screen.fill("light blue")
    a.draw()
    for i in bugs:
        i.draw()

pgzrun.go()