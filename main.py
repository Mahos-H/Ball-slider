import pygame as p
import random
p.init()
w, h = 1000, 600
scr = (w, h)
s = p.display.set_mode(scr)
red = (255, 0, 0)
black = (0, 0, 0)
blue = (0, 0, 255)
br = 10
bp = [100, 100]
bs = [random.randint(1, 2),random.randint(1, 2)]
rw, rh = 160, 10
y = 590  
q=10
x=0
lives=10
font = p.font.Font(None, 36) 
while True:
    br = 10
    bp = [100, 100]
    bs = [random.randint(1, 10),random.randint(1, 10)]
    t=font.render("Number of lives left: "+str(lives), True, red)
    while True:
        
        for event in p.event.get():
            if event.type==p.KEYDOWN and event.key==p.K_q:
                q=0
                break
            if event.type == p.MOUSEMOTION:
                x = event.pos[0] - rw // 2
        if q==0:
            break
        bp[0] += bs[0]
        bp[1] += bs[1]

        if bp[0] - br <= 10 or bp[0]+br>=w-10:
            bs[0] = -bs[0]
            if q==5:
                if bs[0]<=0:
                    bs[0]-=1
                if bs[1]<=0:
                    bs[1]-=1
            if q==1:
                if bs[0]>=0:
                    bs[0]+=1
                if bs[1]>=0:
                    bs[1]+=1
                q=10
            q-=1
            bp[0] += bs[0]
            bp[1] += bs[1]
        if bp[1] - br <= 0:
            bs[1] = -bs[1]
            if q==1:
                if bs[0]!=-1:
                    bs[0]+=1
                if bs[1]!=-1:
                    bs[1]+=1
                q=10
            q-=1
            bp[0] += bs[0]
            bp[1] += bs[1]
        if (bp[0] + br >= x and bp[0]-br<=x+rw) and (bp[1]+br >=590 and bp[1]-br<=600):
            if bp[0] + br < x+ rw//2:
                bs[0] = -bs[0]
            bs[1] = -bs[1]
        elif bp[1]+br>=h:
            lives-=1
            if lives==0:
                print("Game Over")
            else:
                r = t.get_rect(center=(500, 50)) 
                s.blit(t, r)
                p.display.flip()
                p.time.delay(1200)  
            break
        s.fill(black)
        p.draw.circle(s, red, bp, br)
        p.draw.rect(s, blue, (x, y, rw-10, rh))
        p.display.flip()
        p.time.Clock().tick(120)
    if lives==0:
        p.quit()
        break
