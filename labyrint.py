#Koostasid Peeter ja Kristjan, Henrik andis nõu kui meil ideed otsa said


#Vajalikud moodulid
import pygame, sys

#Pygame käima, ekraan, ning pilt, samuti font ja tekst.
pygame.init()
ekraan = pygame.display.set_mode([1000, 1000])
pygame.display.set_caption("Arvestus")
kala = pygame.image.load("kala.png")
#endhalb = pygame.image.load("endscreen.png")
#starthalb = pygame.image.load("startscreen.png")
end = pygame.image.load("endscreen2.png")
start = pygame.image.load("startscreen2.png")
game_over = pygame.image.load("aeg_l2bi.png")

f = pygame.font.SysFont("Calibri", 40)
nr = 50000
#tekst = f.render("Lõpp", 1, [255, 0, 0])
tekst2 = f.render("Skoor: %s" % nr, 1, [255, 255, 255])
#tekst3 = f.render("Mida kõrgem skoor, seda parem.", 1, [255, 0, 0])

#Kala algsed koordinaadid, värvid, pildi kuvamine
#Ekraani värskendamine ning "lohista" väärtus, hiire koordinaatide väärtustamine
x, y = 550, 450
vv2rv = [50, 205, 50]
must = [0, 0, 0]
pun = [255, 0, 0]
kol = [255, 255, 0]
valge = [255, 255, 255]
ekraan.blit(start, (0, 0))
#ekraan.blit(starthalb, (0, 0))
pygame.display.update()
pygame.time.delay(15000)
ekraan.blit(kala, (x, y))
pygame.display.update()
lohista = False
mx, my = pygame.mouse.get_pos()

#Seinade koordinaadid
def sein():
    pygame.draw.rect(ekraan, must, [300, 0, 200, 200])
    pygame.draw.rect(ekraan, must, [100, 100, 100, 200])
    pygame.draw.rect(ekraan, must, [200, 300, 300, 200])
    pygame.draw.rect(ekraan, must, [0, 400, 100, 100])
    pygame.draw.rect(ekraan, must, [800, 0, 100, 500])
    pygame.draw.rect(ekraan, must, [600, 100, 100, 300])
    pygame.draw.rect(ekraan, must, [500, 300, 100, 100])
    pygame.draw.rect(ekraan, must, [400, 500, 300, 100])
    pygame.draw.rect(ekraan, must, [200, 500, 100, 200])
    pygame.draw.rect(ekraan, must, [100, 600, 100, 100])
    pygame.draw.rect(ekraan, must, [100, 800, 100, 200])
    pygame.draw.rect(ekraan, must, [300, 700, 100, 200])
    pygame.draw.rect(ekraan, must, [700, 900, 200, 100])
    pygame.draw.rect(ekraan, must, [500, 700, 400, 100])
    pygame.draw.rect(ekraan, must, [700, 500, 200, 100])
    pygame.draw.rect(ekraan, must, [500, 800, 100, 200])
    pygame.draw.rect(ekraan, pun, [600, 900, 100, 100])
    pygame.draw.rect(ekraan, kol, [500, 400, 100, 100])


roh1 = 1
roh2 = 1
roh3 = 1
roh4 = 1
mus1 = 1


running = True

#Mäng ise...
while running:
    nr = nr - 1
    if nr == 0:
        ekraan.blit(game_over, (0, 0))
        pygame.display.update()
        pygame.time.delay(5000)
        break
    #print (nr)
    tekst2 = (f.render("Skoor: %s" % nr , 1, [255, 255, 255]))
    
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            running = False #Mängu sulgemistsükkel
        elif i.type == pygame.MOUSEBUTTONDOWN:
            mx, my = i.pos
            pygame.mouse.set_visible(False)
            if abs(mx-x)<50 and abs(my-y)<50: #Kontrollib, kas hiir on kala peal
                lohista = True

        elif i.type == pygame.MOUSEBUTTONUP:
            lohista = False #Kui hiirenupp ei ole alla vajutatud
            pygame.mouse.set_visible(True)
            
        elif lohista and i.type == pygame.MOUSEMOTION:
            x, y = i.pos #Hiire koordinaadite andmine x-ile ja y-ile.

    ekraan.fill(valge)

    #Loob seinad

    sein()

    #Kontrollib, kas roh1, roh2 jne väärtus on 1

    if roh1 == 1:
        pygame.draw.rect(ekraan, vv2rv, [300, 500, 100, 100])
    if roh2 == 1:
        pygame.draw.rect(ekraan, vv2rv, [0, 900, 100, 100])
    if roh3 == 1:
        pygame.draw.rect(ekraan, vv2rv, [900, 0, 100, 100])
    if roh4 == 1:
        pygame.draw.rect(ekraan, vv2rv, [900, 900, 100, 100])
    if mus1 == 1:
        pygame.draw.rect(ekraan, must, [600, 800, 100, 100])

    #Kui satub rohelise ruudu koordinaatidele, muudab roh1, roh2 jne väärtust.

    if 0 < abs(x) < 100 and 900 < abs(y) < 1000:
        roh2 = 0

    if 300 < abs(x) < 400 and 500 < abs(y) < 600:
        roh1 = 0

    if 900 < abs(x) < 1000 and 0 < abs(y) < 100:
        roh3 = 0
 
    if 900 < abs(x) < 1000 and 900 < abs(y) < 1000:
        roh4 = 0
        


    if mus1 == 1: #Kui must ruut on lõpu ees
        #Kontrollib, kas hiir on ruudu koordinaatide peal.
        if 580 < abs(x) < 720 and 720 < abs(y) < 920:
            #Kui on, siis pilt liigub algsesse positsiooni ning rohelised ruudud ja must ruut resetivad.
            lohista = False
            x, y = 550, 450
            roh1 = 1
            roh2 = 1
            roh3 = 1
            roh4 = 1
            mus1 = 1
            pygame.display.update()
        #Kui kõik rohelised ruudud on kogutud
        elif roh1 == 0 and roh2 == 0 and roh3 == 0 and roh4 == 0:
            #Kaotab musta ruutu
            mus1 = 0
        
    ekraan.blit(kala, (x-20,y-20))
    pygame.display.update()

    #Kontrollib iga seina juures, kas hiire koordinaadid kattuvad seina koordinaatidega.
    #Kui kattuvad, siis pilt liigub algsesse positsiooni ning rohelised ruudud ning must ruut resetivad.

    if 280 < abs(x) < 520 and 0 < abs(y)< 220:
        lohista = False
        x, y = 550, 450
        roh1 = 1
        roh2 = 1
        roh3 = 1
        roh4 = 1
        mus1 = 1
        pygame.display.update()
        
    elif 80 < abs(x) < 220 and 80 < abs(y) < 320:
        lohista = False
        x, y = 550, 450
        roh1 = 1
        roh2 = 1
        roh3 = 1
        roh4 = 1
        mus1 = 1
        pygame.display.update()
        
    elif 580 < abs(x) < 720 and 80 < abs(y) < 420:
        lohista = False
        x, y = 550, 450
        roh1 = 1
        roh2 = 1
        roh3 = 1
        roh4 = 1
        mus1 = 1
        pygame.display.update()
        
    elif 180 < abs(x) < 620 and 280 < abs(y) < 420:
        lohista = False
        x, y = 550, 450
        roh1 = 1
        roh2 = 1
        roh3 = 1
        roh4 = 1
        mus1 = 1
        pygame.display.update()
        
    elif 180 < abs(x) < 520 and 380 < abs(y) < 520:
        lohista = False
        x, y = 550, 450
        roh1 = 1
        roh2 = 1
        roh3 = 1
        roh4 = 1
        mus1 = 1
        pygame.display.update()
        
    elif 0 < abs(x) < 120 and 380 < abs(y) < 520:
        lohista = False
        x, y = 550, 450
        roh1 = 1
        roh2 = 1
        roh3 = 1
        roh4 = 1
        mus1 = 1
        pygame.display.update()
        
    elif 180 < abs(x) < 320 and 480 < abs(y) < 720:
        lohista = False
        x, y = 550, 450
        roh1 = 1
        roh2 = 1
        roh3 = 1
        roh4 = 1
        mus1 = 1
        pygame.display.update()
        
    elif 80 < abs(x) < 220 and 580 < abs(y) < 720:
        lohista = False
        x, y = 550, 450
        roh1 = 1
        roh2 = 1
        roh3 = 1
        roh4 = 1
        mus1 = 1
        pygame.display.update()
        
    elif 80 < abs(x) < 220 and 780 < abs(y) < 1000:
        lohista = False
        x, y = 550, 450
        roh1 = 1
        roh2 = 1
        roh3 = 1
        roh4 = 1
        mus1 = 1
        pygame.display.update()
        
    elif 280 < abs(x) < 420 and 680 < abs(y) < 920:
        lohista = False
        x, y = 550, 450
        roh1 = 1
        roh2 = 1
        roh3 = 1
        roh4 = 1
        mus1 = 1
        pygame.display.update()
        
    elif 380 < abs(x) < 920 and 480 < abs(y) < 620:
        lohista = False
        x, y = 550, 450
        roh1 = 1
        roh2 = 1
        roh3 = 1
        roh4 = 1
        mus1 = 1
        pygame.display.update()
        
    elif 780 < abs(x) < 920 and 0 < abs(y) < 520:
        lohista = False
        x, y = 550, 450
        roh1 = 1
        roh2 = 1
        roh3 = 1
        roh4 = 1
        mus1 = 1
        pygame.display.update()
        
    elif 680 < abs(x) < 920 and 880 < abs(y) < 1000:
        lohista = False
        x, y = 550, 450
        roh1 = 1
        roh2 = 1
        roh3 = 1
        roh4 = 1
        mus1 = 1
        pygame.display.update()
        
    elif 480 < abs(x) < 920 and 680 < abs(y) < 820:
        lohista = False
        x, y = 550, 450
        roh1 = 1
        roh2 = 1
        roh3 = 1
        roh4 = 1
        mus1 = 1
        pygame.display.update()
        
    elif 480 < abs(x) < 620 and 780 < abs(y) < 1000:
        lohista = False
        x, y = 550, 450
        roh1 = 1
        roh2 = 1
        roh3 = 1
        roh4 = 1
        mus1 = 1
        pygame.display.update()

    #Kui jõutakse punase ruuduni, väljastatakse tekst.

    if 600 < abs(x) < 700 and 900 < abs(y) < 1000:
        ekraan.blit(end, (0, 0))
        #ekraan.blit(endhalb, (0, 0))
        #ekraan.blit(tekst3, [370, 350])
        ekraan.blit(tekst2, [400, 600])
        pygame.display.update()
        #print ("Skoor:",nr,"/ 50000")
        #Delay enne break'i, et jõuaks vaadata lõpuekraani.
        pygame.time.delay(5500)
        break


pygame.quit()