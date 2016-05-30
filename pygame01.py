import pygame

pygame.init()

# define display dimensions
display_width = 800
display_height = 600

# define colors
black = (0, 0, 0)
white = (255, 255, 255)
red = (255,0,0)

# create window object with len/width
gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('A bit Racey!')

# start fps clock object
clock = pygame.time.Clock()

race_car_path = "001.png"
carImg = pygame.image.load(race_car_path)


def car (x,y):
    # draw an image; format
    # <img path> <x-y coord tuple>
    # NOTE:
    # X: + moves right, - moves down
    # Y: + moves down, - moves up
    gameDisplay.blit(carImg,(x,y))

x = (display_width * 0.45)
y = (display_height * 0.8)

# in this game if you have crashed, you lose
crashed = False
# don't crash idiot
while not crashed:

    # checking for input events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:

        print event

    gameDisplay.fill(white)
    car(x,y)
    pygame.display.update()
    # fps tick
    clock.tick(60)

pygame.quit()
