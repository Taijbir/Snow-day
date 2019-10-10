#Taijbir's Legend of Zelda Assignment

#background$/color$
#boundaries$/ mazes$
#obstacles/enemies
#treasure
'''
Level 1/2
1 Map#$
 Maze#$
Collisions$
Move$ + animation$
colour$
background image$

Level 3
Music$ + Effects$
At least 1 treasure with textbox
textbox$
Obstacles + at least 3 moving Enemies

Level 4
2 Maps with all features spread out and a map transition animation
'''
    
import pygame
import random
pygame.init()
myfont= pygame.font.SysFont("exo_font.zip", 50)
myfont2= pygame.font.SysFont("exo_font.zip", 30)
myfont3= pygame.font.SysFont("exo_font.zip", 15)
win = pygame.display.set_mode((800,600))
pygame.display.set_caption("Snow Day")

#Animation images
walkRight = [pygame.image.load('R1.png'), pygame.image.load('R2.png'),
             pygame.image.load('R3.png'), pygame.image.load('R4.png'),
             pygame.image.load('R5.png'), pygame.image.load('R6.png'),
             pygame.image.load('R7.png'), pygame.image.load('R8.png'),
             pygame.image.load('R9.png')]
walkLeft = [pygame.image.load('L1.png'), pygame.image.load('L2.png'),
            pygame.image.load('L3.png'), pygame.image.load('L4.png'),
            pygame.image.load('L5.png'), pygame.image.load('L6.png'),
            pygame.image.load('L7.png'), pygame.image.load('L8.png'),
            pygame.image.load('L9.png')]
#background image
bg = pygame.image.load('winter1.jpg')
#characterz standing image
char = pygame.image.load('standing.png')
#music
music = pygame.mixer.music.load('music_py.ogg')
pygame.mixer.music.play(loops=-1)
#house image
house = pygame.image.load('house.png')
#badguy
badGuy = pygame.image.load('L1E.png')

#variables
x = 50
y = 500
width = 40
height = 60
vel = 5
winWidth = 800
winHeight = 600
clock = pygame.time.Clock()

#if using title page code keep otherwise delete
white=(255,255,255)
black = (0,0,0)
red= (200,0,0)
green=(0,200,0)
bright_red =(255,0,0)
bright_green= (0,255,0)
########

left = False
right = False
up = False
down = False
walkCount = 0

fall_list = []

#all drawings and animations
def redrawGameWindow():
    global walkCount
    win.blit(bg, (0,0))#background
    win.blit(house, (715, 500))
    win.blit(badGuy, (140, 3))
    win.blit(badGuy, (340, 3))
    win.blit(badGuy, (540, 3))
    #snowing effect 
    bad_X = random.randrange(0,winWidth)
    bad_Y = random.randrange(0, winHeight)
    fall_list.append([bad_X, bad_Y])
    for i in range(len(fall_list)):
        pygame.draw.circle(win, white, fall_list[i], 2)
        fall_list[i][1] += 1
        if fall_list[i][1] > winHeight:
            bad_Y = random.randrange(-50, -10)
            fall_list[i][1] = bad_Y
            bad_X = random.randrange(0, 800)
            fall_list[i][0] = bad_X
   #walking animation
    if walkCount + 1 >= 27:
        walkCount = 0
    if left:  
        win.blit(walkLeft[walkCount//3], (x,y))
        walkCount += 1                          
    elif right:
        win.blit(walkRight[walkCount//3], (x,y))
        walkCount += 1
    elif up:
        win.blit(walkRight[walkCount//3], (x,y))
        walkCount += 1
    elif down:  
        win.blit(walkLeft[walkCount//3], (x,y))
        walkCount += 1  
    else:
        win.blit(char, (x, y))
        walkCount = 0
    #drawings
    pygame.draw.rect(win,(138,43,226), (100, 0, 50, 340))#light purple wall
    pygame.draw.rect(win,(70,130,180), (300, 0, 50, 340))#steel blue wall
    pygame.draw.rect(win,(128, 0, 128), (500, 0, 50, 340)) #dark purple wall
    pygame.draw.rect(win,(245, 245, 220), (650, 100, 50, 500)) #beige  wall
    pygame.draw.rect(win,(0,191,255), (400, 100, 50, 500)) #light blue wall
    pygame.draw.rect(win,(106,90,205), (200, 100, 50, 500)) #blue purple wall
    #texts
    text_1=myfont.render("Snow Day - Level 1",1,(200,255,255))
    win.blit(text_1,(250,10))
    text_2=myfont2.render("Get Home!",1,(100,255,255))
    win.blit(text_2,(350,50))
    text_3=myfont3.render("Continue to Level 2",1,(200,255,255))
    win.blit(text_3,(700,490))
    pygame.display.update()
    
#main loop
run = True


##def text_objects(text, font):
##    textSurface = font.render(text, True, black)
##    return textSurface, textSurface.get_rect()
##def button(msg,x,y,w,h,ic,ac,action=None):
##    mouse =pygame.mouse.get_pos()
##    click = pygame.mouse.get_pressed()
##    print(click)
##    if x+w > mouse[0] > x and y+h > mouse[1] > y:
##        pygame.draw.rect(win,ac,(x,y,w,h))
##        if click[0] == 1 and action != None:
##            if action == "play":
##                redrawGameWindow()
##                intro = False
##            elif action == "quit":
##                pygame.quit()
##                quit()
##    else:
##        pygame.draw.rect(win,ic,(x,y,w,h))
##    smallText= pygame.font.SysFont("exo_font.zip",20)
##    textSurf, textRect = text_objects(msg, smallText)
##    textRect.center = ( (x+(w/2)), y+(h/2))
##    win.blit(textSurf, textRect)
##
##def game_intro():
##
##    intro = True
##
##    while intro:
##        for event in pygame.event.get():
##            #print(event)
##            if event.type == pygame.QUIT:
##                pygame.quit()
##                quit()
##                
##        win.fill(white)
##        largeText = pygame.font.SysFont("exo_font.zip", 115)
##        TextSurf, TextRect = text_objects("LEGENDS", largeText)
##        TextRect.center = ((800/2),(600/2))
##        win.blit(TextSurf, TextRect)
##        button("START",150,450,100,50,green,bright_green, "play")
##        button("QUIT",550,450,100,50,red,bright_red,"quit")
##        pygame.display.update()
##        clock.tick(15)
##
##game_intro()

while run:
    clock.tick(27)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and x > vel: 
        x -= vel
        left = True
        right = False
        if x>50 and x<135 and y<325: #light purple wall
            x = 135
        elif x>250 and x<340 and y<325: #steel blue wall
            x = 340
        elif x>450 and x<540 and y<325: #dark purple wall
            x = 540
        elif x>600 and x<685 and y>50:  #beige  wall
            x = 685
        elif x>350 and x<435 and y>50: #light blue wall
            x = 435
        elif x>150 and x<235 and y>50:  #blue purple wall
            x = 235
    elif keys[pygame.K_RIGHT] and x < 800 - vel - width:   
        x += vel
        left = False
        right = True
        if x>50 and x<135 and y<325:  #light purple wall
            x = 50
        elif x>250 and x<300 and y<325:  #steel blue wall
            x = 250
        elif x>450 and x<500 and y<325: #dark purple wall
            x = 450
        elif x>600 and x<685 and y>50: #beige  wall
            x = 600
        elif x>350 and x<435 and y>50:  #light blue wall
            x = 350
        elif x>150 and x<235 and y>50: #blue purple wall
            x = 150
    elif keys[pygame.K_UP] and y > vel:  
        y -= vel
        up = True
        down = False
        if x>50 and x<125 and y<335:  #light purple wall
            y = 325
        elif x>250 and x<325 and y<335:  #steel blue wall
            y = 325
        elif x>450 and x<525 and y<335: #dark purple wall
            y = 325  
    elif keys[pygame.K_DOWN] and y < 600 - height - vel:
        y += vel
        up = False
        down = True
        if x>600 and x<685 and y>40:  #beige  wall
            y = 40
        elif x>350 and x<435 and y>40:  #light blue wall
            y = 40
        elif x>150 and x<235 and y>40:  #blue purple wall
            y = 40
    else:
        left = False
        right = False
        up = False
        down =False
        walkCount = 0
    redrawGameWindow()
pygame.quit()

