import pygame
from pygame.draw import rect
import time
import button

pygame.init()

#Screen
SCREEN_WIDTH = 1050
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

#Font for text
font = pygame.font.SysFont("arial", 32)
font2 = pygame.font.SysFont("arial", 62)
#colors for disks
colors = ["red", "green", "blue", "purple", "black", "brown", "yellow", "orange"]

#Title and Icon
color = (52, 72, 91)
pygame.display.set_caption('Tower of Hanoi')
Icon = pygame.image.load('images/icon.png')
pygame.display.set_icon(Icon)

#Game variabiles

Tower1 =[]
Tower2 = []
Tower3 = []
position = []
objects_rect = []
DISC_NUMBER = 3
active_disc = None
precedentTower = None
moves = 0
game_paused = False

#load button images

resume_img = pygame.image.load("images/resume.png").convert_alpha()
menu_img = pygame.image.load("images/menu.png").convert_alpha()
solve_img = pygame.image.load("images/solve.png").convert_alpha()
quit_img = pygame.image.load("images/quit.png").convert_alpha()
up_img = pygame.image.load("images/up.png").convert_alpha()
down_img = pygame.image.load("images/down.png").convert_alpha()
restart_img = pygame.image.load("images/restart.png").convert_alpha()
num = pygame.image.load('images/num.png')
TowerImg = pygame.image.load('images/towers.png').convert()

#create buttons

resume_button = button.Button(380, 125, resume_img, 1)
menu_button = button.Button(850, 20, menu_img, 1)
solve_button = button.Button(380, 240, solve_img, 1)
quit_button = button.Button(380, 355, quit_img, 1)
up_button = button.Button(200, 20, up_img, 1)
down_button = button.Button(250, 20, down_img, 1)
restart_button = button.Button(650, 20, restart_img, 1)


#Create Towers
def Towers(img, rect):
    pygame.Surface.set_colorkey(img, [255, 255, 255])
    screen.blit(TowerImg, rect)

rect1 = TowerImg.get_rect()
rect1.center = 180, 360

rect2 = TowerImg.get_rect()
rect2.center = 520, 360

rect3 = TowerImg.get_rect()
rect3.center = 860, 360

#Create Discs

W = 75
H = 24
X = rect1.centerx - (W // 2)
Y = rect1.bottom - (H + DISC_NUMBER*H)
for i in range(DISC_NUMBER):
    position.append((X, Y))
    objects_rect.append(pygame.Rect(X, Y, W, H))
    W = W + 30
    X = X - 15
    Y = Y + 24

for i in range(DISC_NUMBER - 1, -1, -1):
    Tower1.append(objects_rect[i])
def create_discs():
    for i, disc in enumerate(objects_rect):
        pygame.draw.rect(screen, colors[i], disc)

#Check for collisions
def check_collision(rect1, rect2):
    return rect1.colliderect(rect2)

#draw the text
def draw_text(text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    screen.blit(img, (x, y))

#draw for solve
def draw():

    screen.fill(color)
    Towers(TowerImg, rect1)
    Towers(TowerImg, rect2)
    Towers(TowerImg, rect3)

    global moves
    moves += 1
    draw_text("Moves :" + str(moves), font, (255, 255, 255), 25, 525)
    create_discs()
    pygame.display.flip() #switch the display

#Move the discs
def move_disc(num, tower):

    if tower == "Tower1":
        Tower1.append(objects_rect[num])
        position[num] = (rect1.centerx - objects_rect[num].width // 2, rect1.bottom - (
                objects_rect[num].height + len(Tower1) * objects_rect[num].height))
        objects_rect[num].topleft = position[num]

    elif tower == "Tower2":
        Tower2.append(objects_rect[num])
        position[num] = (rect2.centerx - objects_rect[num].width // 2, rect2.bottom - (
                objects_rect[num].height + len(Tower2) * objects_rect[num].height))
        objects_rect[num].topleft = position[num]

    elif tower == "Tower3":
        Tower3.append(objects_rect[num])
        position[num] = (rect3.centerx - objects_rect[num].width // 2, rect3.bottom - (
                objects_rect[num].height + len(Tower3) * objects_rect[num].height))
        objects_rect[num].topleft = position[num]

#Computer move
def hanoi_move(first, second):

    if first == "Tower1":
        num = objects_rect.index(Tower1[len(Tower1) - 1])
        if second == "Tower2":
            Tower1.pop()
            move_disc(num, "Tower2")

        elif second == "Tower3":
            Tower1.pop()
            move_disc(num, "Tower3")

    if first == "Tower2":
        num = objects_rect.index(Tower2[len(Tower2) - 1])
        if second == "Tower1":
            Tower2.pop()
            move_disc(num, "Tower1")

        elif second == "Tower3":
            Tower2.pop()
            move_disc(num, "Tower3")

    elif first == "Tower3":
        num = objects_rect.index(Tower3[len(Tower3) - 1])
        if second == "Tower1":
            Tower3.pop()
            move_disc(num, "Tower1")


        elif second == "Tower2":
            Tower3.pop()
            move_disc(num, "Tower2")

    draw()
    time.sleep(0.4)

#hanoi function
def hanoi(n,a,b,c):
    if n==1:
        hanoi_move(a,b)
    else:
        hanoi(n-1,a,c,b)
        hanoi_move(a,b)
        hanoi(n-1,c,b,a)

def restart(var):
    global game_paused, Tower1, Tower2, Tower3, active_disc, precedentTower, moves, position, objects_rect, W, H, X, Y
    game_paused = False
    Tower1 = []
    Tower2 = []
    Tower3 = []
    active_disc = None
    precedentTower = None
    moves = 0

    position = []
    objects_rect = []

    W = 75
    H = 24
    X = rect1.centerx - (W // 2)
    Y = rect1.bottom - (H + var * H)

    for i in range(var):
        position.append((X, Y))
        objects_rect.append(pygame.Rect(X, Y, W, H))
        W = W + 30
        X = X - 15
        Y = Y + 24

    for i in range(var - 1, -1, -1):
        Tower1.append(objects_rect[i])


running = True

#Game loop
while running:

    screen.fill(color)

    #if menu button is pressed
    if game_paused == True:
        if resume_button.draw(screen):  #pause menu
            game_paused = False

        if solve_button.draw(screen): #solve the game

            #restart the game variabiles
            restart(DISC_NUMBER)

            hanoi(DISC_NUMBER, "Tower1", "Tower3", "Tower2")


        if quit_button.draw(screen): #exit the game
            running = False


    else:
        if restart_button.draw(screen):
            # restart the game variabiles
            restart(DISC_NUMBER)

        if up_button.draw(screen) and DISC_NUMBER < 8: #increase the number of discs

            # restart the game variabiles
            DISC_NUMBER += 1
            restart(DISC_NUMBER)

        elif down_button.draw(screen) and DISC_NUMBER > 1: #decrease the number of discs

            # restart the game variabiles
            DISC_NUMBER -= 1
            restart(DISC_NUMBER)

        if menu_button.draw(screen): #if the menu button is pressed
            game_paused = True

        #Principal screen

        MINIMUM_MOVES = 2**DISC_NUMBER - 1 #minimum moves

        draw_text("Moves :" + str(moves), font, (255, 255, 255), 25, 525)
        draw_text("Minimum no. of moves : " + str(MINIMUM_MOVES ), font, (255, 255, 255), 600, 525)
        screen.blit(num, (120, 20))
        draw_text("  Discs:   " + str(DISC_NUMBER), font, (255, 255, 255), 15, 25)

        Towers(TowerImg, rect1)
        Towers(TowerImg, rect2)
        Towers(TowerImg, rect3)
        create_discs()

        if len(Tower3) == DISC_NUMBER:
            draw_text("Great Job!!", font2, (255, 255, 255), 370, 100) #Final of the game

    #events
    for event in pygame.event.get():

        if event.type == pygame.MOUSEBUTTONDOWN: #if a disc is clicked

            if event.button == 1:
                if len(Tower1) != 0:
                    if Tower1[len(Tower1) - 1].collidepoint(event.pos): #first tower is clickef
                        active_disc = objects_rect.index(Tower1[len(Tower1) - 1]) #set the active disc clicked
                        precedentTower = "Tower1"
                        Tower1.pop()

                if len(Tower2) != 0:
                    if Tower2[len(Tower2) - 1].collidepoint(event.pos): #second tower is clickef
                        active_disc = objects_rect.index(Tower2[len(Tower2) - 1])
                        precedentTower = "Tower2"
                        Tower2.pop()

                if len(Tower3)!= 0:
                    if Tower3[len(Tower3) - 1].collidepoint(event.pos): #third tower is clickef
                        active_disc = objects_rect.index(Tower3[len(Tower3) - 1])
                        precedentTower = "Tower3"
                        Tower3.pop()

        if event.type == pygame.MOUSEMOTION: #move the disc
            if active_disc != None:
                objects_rect[active_disc].move_ip(event.rel)

        if event.type == pygame.MOUSEBUTTONUP: #put the disc in a certain place

            if active_disc != None:
                if check_collision(objects_rect[active_disc], rect1):
                    if len(Tower1) != 0:

                        if objects_rect[active_disc].width < Tower1[len(Tower1) - 1].width: #if the active disc is smaller
                            move_disc(active_disc, "Tower1") #move the disc to the tower1
                            if precedentTower != "Tower1":
                                moves += 1
                        else:
                            move_disc(active_disc, precedentTower) #move the disc back to his position


                    else:
                        move_disc(active_disc, "Tower1")
                        if precedentTower != "Tower1":
                            moves += 1

                elif check_collision(objects_rect[active_disc], rect2):
                    if len(Tower2) != 0:

                        if objects_rect[active_disc].width < Tower2[len(Tower2) - 1].width: #if the active disc is smaller
                            move_disc(active_disc, "Tower2") #move the disc to the tower2
                            if precedentTower != "Tower2":
                                moves += 1
                        else:
                            move_disc(active_disc, precedentTower)

                    else:
                        move_disc(active_disc, "Tower2")
                        if precedentTower != "Tower2":
                            moves += 1

                elif check_collision(objects_rect[active_disc], rect3):
                    if len(Tower3) != 0:

                        if objects_rect[active_disc].width < Tower3[len(Tower3) - 1].width: #if the active disc is smaller
                            move_disc(active_disc, "Tower3") #move the disc to the tower3
                            if precedentTower != "Tower3":
                                moves += 1
                        else:
                            move_disc(active_disc, precedentTower) #move the disc back to his position

                    else:
                        move_disc(active_disc, "Tower3")
                        if precedentTower != "Tower3":
                            moves += 1

                else:
                    move_disc(active_disc, precedentTower) #move the disc back to his position

            if event.button == 1:
                active_disc = None

        if event.type == pygame.QUIT:
            running = False

    pygame.display.flip() #update display
