#importing stuff for the program
import random
import pygame
import time

#initiating pygame and font
WHITE = (255, 255, 255)
SCREEN_WIDTH = 300
SCREEN_HEIGHT = 200
pygame.init()
screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
lastchoicetime = 0
minimumtime = .1

#contains a list of every kid in the class; that will not change
allKids = ["Sophie", "Colton", "Julia", "Isaac", "Owen", "Rose",
         "Jillian", "Paisley", "Lily", "Samson", "Lucas", "Sophia",
              "Sven", "Grace", "JM", "Violet", "Carson", "Stephen",
              "Caden", "Abby", "Ella", "Wade", "Reed"]

# hungrykids contains a list of kids who have not eaten
hungrykids = []

# fedkids is a list of kids who have eaten
fedkids = []

#functions
def startScreen(kid):
    myfont = pygame.font.SysFont("georgia", 18)
    intro = myfont.render("Snackerator 9000 TM", 1, (255, 0, 0))
    yourname = myfont.render(kid, 1, (255, 0, 0))
    alexSubtitle = myfont.render("Alex also made this", 1, (255, 0, 0))
    screen.blit(intro, (50, 10))
    screen.blit(alexSubtitle, (150, 180))
    screen.blit(yourname, (100, 40))
    clickbutton = myfont.render("Click Space for Next Kid.", 1, (255, 0, 0))
    screen.blit(clickbutton, (50,75))
    enjoy = myfont.render("Enjoy Your Snack!", 1, (255, 0, 0))
    screen.blit(enjoy, (50, 150))
    reset = myfont.render("Click R to Reset", 1, (255, 0, 0))
    screen.blit(reset, (50, 115))

def resetKids():
    global hungrykids
    hungrykids = []
    for i in allKids:
        hungrykids.append(i)

def removeKid():
    global lastchoicetime
    now = time.time()
    dif = now - lastchoicetime
    if dif > minimumtime:
        lastchoicetime = time.time()
        kid = random.choice(hungrykids)
        hungrykids.remove(kid)
        fedkids.append(kid)
        startScreen(kid)
        pygame.display.flip()
        return kid

#list of kids who need to have snack
hungrykids = ["Sophie", "Colton", "Julia", "Isaac", "Owen", "Rose",
         "Jillian", "Paisley", "Lily", "Samson", "Lucas", "Sophia",
              "Sven", "Grace", "JM", "Violet", "Carson", "Stephen",
              "Caden", "Abby", "Ella", "Wade", "Reed"]

#Starts up Kid list
resetKids()

# Set up screen
screen.fill(WHITE)
startScreen("Press Space")
pygame.display.flip()

#This is how the code works
while True: 
    for event in pygame.event.get():
        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
            pygame.quit()
        if keys[pygame.K_SPACE]:
            screen.fill(WHITE)
            if len(hungrykids) > 0:
                kid = removeKid()
                if kid:
                    print kid, " for snack!", len(hungrykids), " left."
                else:
                    print "slow down, little jimmy!"
            if len(hungrykids) == 0:
                print "Snack is over!"
        if keys[pygame.K_l]:
            screen.fill(WHITE)
            hungrykids.append(kid)
            removeKid()
        if keys[pygame.K_r]:
            resetKids()
            screen.fill(WHITE)
            startScreen("Press Space")
            pygame.display.flip()
