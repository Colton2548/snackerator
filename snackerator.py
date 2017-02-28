#Goals: List of names, Pick one randomly, Delete each one as they're
#picked
#Reset the list, "trigger" button (2)
import random

#initiating pygame and font
import pygame
WHITE = (255, 255, 255)
SCREEN_WIDTH = 300
SCREEN_HEIGHT = 200
pygame.init()
screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])


#other stuff
hungrykids = ["Sophie", "Colton", "Julia", "Isaac", "Owen", "Rose",
         "Jillian", "Paisley", "Lily", "Samson", "Lucas", "Sophia",
              "Sven", "Grace", "JM", "Violet", "Carson", "Stephen",
              "Caden", "Abby", "Ella", "Wade", "Reed"]
random.shuffle(hungrykids)
print hungrykids

while True: 
    for event in pygame.event.get():
        keys = pygame.key.get_pressed()
        if keys[27]:
            pygame.quit()
    screen.fill(WHITE)

    myfont = pygame.font.SysFont("georgia", 18)
    intro = myfont.render("Snackerator 9000 TM", 1, (255, 0, 0))
    yourname = myfont.render("Name", 1, (255, 0, 0))
    screen.blit(intro, (50, 10))
    screen.blit(yourname, (100, 40))
    clickbutton = myfont.render("Click Space for Next Kid.", 1, (255, 0, 0))
    screen.blit(clickbutton, (50,75))
    enjoy = myfont.render("Enjoy Your Snack!", 1, (255, 0, 0))
    screen.blit(enjoy, (50, 150))
    reset = myfont.render("Click R to Reset", 1, (255, 0, 0))
    screen.blit(reset, (50, 115))

    pygame.display.flip()
