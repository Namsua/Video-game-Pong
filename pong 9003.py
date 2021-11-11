import pygame
import random

pygame.mixer.pre_init(44100, -16, 2, 2048)
pygame.init()
clock = pygame.time.Clock() #Kell. Et fps-i määrata. Saab ka arvutusi teha, aga meil mitte :(

ekraan = pygame.display.set_mode ((640, 480))
pygame.display.set_caption("Old School Pong")

reket1 = pygame.Rect(0,170,10,100)

pygame.display.flip()


yrec1 = 170     #vasaku reketi y koordinaat
yrec2 = 170     #parema reketi y koordinaat
x = 310         #palli x koordinaat
y = 220         #pally y koordinaat
palli_kiirus = 3
ai_kiirus = 2
player_kiirus = 4
r2ndom = 1
r2ndom2 = 3-r2ndom
suund = 4       #algne suund, et pall teaks kuhu minna, mida oma eluga peale hakata 
yrec1lubatud = [240]       #see list on vajalik, et määrata vasaku reketi "mõjuala", ala, millelt pall tagasi põrkab
yrec2lubatud = []
skoorplayer = 0
skoorAI = 0

pygame.key.set_repeat(1, 3) #Paneb nupuvajutuse kordama. Parem oleks pygame.key.get_pressed(), aga ei saanud tööle

def reset():
    if event.key == pygame.K_SPACE:
        global skoorplayer
        skoorplayer = 0
        global skoorAI
        skoorAI = 0
        global yrec1lubatud
        yrec1lubatud = [240]
        global reket1
        global yrec1
        yrec1 = 170
        reket1 = pygame.Rect(0,170,10,100)
        pygame.draw.rect(ekraan, (255,255,255), reket1)
        pygame.display.update()
    if event.key == pygame.QUIT: #saab akna kinni panna
        quit()
    if event.key == pygame.K_ESCAPE: #et saaks iga kell välja ESC klahviga
        exit()
    
try:
    while True:
        clock.tick(100)
        ekraan.fill((0,0,0)) #Ekraan tuleb iga kord uuendada, muidu parempoolne reket ei kustuta eelmisi kujutisi.
        
        #vasak "reket"
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                reset()
                if event.key == pygame.K_DOWN:
                    yrec1lubatud = []
                    if  yrec1 < 372:
                        yrec1 +=player_kiirus
                        for i in range(yrec1-10, yrec1+120):
                            yrec1lubatud.append(i)
                        reket1 = pygame.Rect(0,yrec1,10,100)
                    else:
                        yrec1 -= 5
                
                if event.key == pygame.K_UP:
                    yrec1lubatud = []
                    if yrec1 > 6:
                        yrec1 -=player_kiirus
                        for i in range(yrec1-10, yrec1+120):
                            yrec1lubatud.append(i)
                        reket1 = pygame.Rect(0,yrec1,10,100)
                    else:
                        yrec1 += 5
                
            
        pygame.draw.rect(ekraan, (255,255,255), reket1)
        #parem "reket"
        yrec2lubatud = []
        if x>300:   #hakkab liikuma alles siis, kui pall on oma poolel.
            #Kui pall on kõrgemal, liigub kõrgemale, kui madalamal, madalamale.
            if yrec2>y:
                yrec2 -= ai_kiirus
            elif yrec2<y:
                yrec2 += ai_kiirus
        else:
            if yrec2>170:
                yrec2 -= 1
            elif yrec2<170:
                yrec2 += 1
            else:
                yrec2 +=0
        for i in range(yrec2-10, yrec2+110):
            yrec2lubatud.append(i)

        reket2 = pygame.Rect(630, yrec2, 10, 100)
        pygame.draw.rect(ekraan, (255,255,255), reket2)

        pygame.time.wait(2)
    
        pygame.draw.circle(ekraan, (255,255,255), (x,y), 10)
        #keral/pallil on viis liikumissuunda: 0 on üles+vasakule, 1 on alla+paremale, 2 on alla+vasakule, 3 on üles+paremale, 4 on algne
        if suund == 0:
            x -= palli_kiirus*r2ndom2
            y -= palli_kiirus*r2ndom
            if x <= 20 and y in yrec1lubatud:
                suund = 3
            elif x <= 20 and y not in yrec1lubatud:
                skoorAI += 1
                x = 310
                suund = 4
            if y <= 5:
                r2ndom = random.randrange(1, 3)
                suund = 2
            
        elif suund == 1:
            x += palli_kiirus*r2ndom2
            y += palli_kiirus*r2ndom
            if x >= 620 and y in yrec2lubatud:
                suund = 2
            elif x >= 620 and y not in yrec2lubatud:
                skoorplayer += 1
                x = 310
                suund = 4
            if y <= 5:
                r2ndom = random.randrange(1, 3)
                suund = 2
            if y >= 475:
                r2ndom = random.randrange(1, 3)
                suund = 3
            
        elif suund == 2:
            x -= palli_kiirus*r2ndom2
            y += palli_kiirus*r2ndom
            if x <= 20 and y in yrec1lubatud:
                suund = 1
            elif x <= 20 and y not in yrec1lubatud:
                skoorAI += 1
                x = 310
                suund = 4
            if y >= 475:
                r2ndom = random.randrange(1, 3)
                suund = 0
            
        elif suund == 3:
            x += palli_kiirus*r2ndom2
            y -= palli_kiirus*r2ndom
            if x >= 610 and y in yrec2lubatud:
                suund = 0
            elif x >= 610 and y not in yrec2lubatud:
                skoorplayer += 1
                x = 310
                suund = 4
            if y <= 5:
                r2ndom = random.randrange(1, 3)
                suund = 1
            
        elif suund == 4:
            x -= palli_kiirus 
            y = 240
            if x <= 20 and y in yrec1lubatud:
                suund = 1
            
            elif x <= 20 and y not in yrec1lubatud:
                skoorAI += 1
                x = 310
                suund = 4
        
        meie_font = pygame.font.SysFont("Arial", 36)
        tekstplayer = meie_font.render(str(skoorplayer), False, (255,255,255))
        ekraan.blit(tekstplayer, (140, 10))
        tekstAI = meie_font.render(str(skoorAI), False, (255,255,255))
        ekraan.blit(tekstAI, (500, 10))

        if skoorplayer == 3 or skoorAI == 3:
            font2 = pygame.font.SysFont("Arial", 24)
            uuesti = font2.render("Uuesti (SPACE)", False, (255,255,255))
            uuesti_keskel = uuesti.get_rect(center=(640/2, 100))
            välju = font2.render("Välju (ESC)", False, (255,255,255))
            välju_keskel = välju.get_rect(center=(640/2, 130))
            ekraan.blit(uuesti, uuesti_keskel)
            ekraan.blit(välju, välju_keskel)
            pygame.display.update()
            if skoorplayer == 3 or skoorAI == 3:
                event = pygame.event.wait()
                if event.type == pygame.KEYDOWN:
                    reset()
                    
                    
                
        pygame.display.update()


except KeyboardInterrupt:
    print ("cancel")
            
                    
    
    
