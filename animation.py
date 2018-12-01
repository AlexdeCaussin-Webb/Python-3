import pygame, sys, time
from pygame.locals import *

# Set up pygame.
pygame.init()

# Set up the window.
WINDOWWIDTH = 400
WINDOWHEIGHT = 400
windowSurface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT), 0, 32)
pygame.display.set_caption('Modified Animation')

# Set up direction variables.
DOWNLEFT = 'downleft'
DOWNRIGHT = 'downright'
UPLEFT = 'upleft'
UPRIGHT = 'upright'

MOVESPEED = 4

# Set up the colors.
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Set up the box data structure.
b1 = {'rect':pygame.Rect(300, 80, 50, 100), 'color':RED, 'dir':UPRIGHT}
b2 = {'rect':pygame.Rect(200, 200, 20, 20), 'color':GREEN, 'dir':UPLEFT}
b3 = {'rect':pygame.Rect(100, 150, 60, 60), 'color':BLUE, 'dir':DOWNLEFT}
boxes = [b1, b2, b3]

# Set up the circle data structure.

c1 = {'rect':pygame.Rect(50, 100, 45, 45), 'color':RED, 'dir':DOWNRIGHT}
c2 = {'rect':pygame.Rect(20, 20, 20, 20), 'color':BLUE, 'dir': UPRIGHT}
circles = [c1, c2]

# Run the game loop.
while True:
    # Check for the QUIT event.
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    # Draw the white background onto the surface.
    windowSurface.fill(WHITE)

    for b in boxes and c in circles:
        # Move the box data structure.
        if b['dir'] == DOWNLEFT:
            b['rect'].left -= MOVESPEED
            b['rect'].top += MOVESPEED
        if b['dir'] == DOWNRIGHT:
            b['rect'].left += MOVESPEED
            b['rect'].top += MOVESPEED
        if b['dir'] == UPLEFT:
            b['rect'].left -= MOVESPEED
            b['rect'].top -= MOVESPEED
        if b['dir'] == UPRIGHT:
            b['rect'].left += MOVESPEED
            b['rect'].top -= MOVESPEED

        # Move the circle data structure.
        if c['dir'] == DOWNLEFT:
            c['rect'].left -= MOVESPEED
            c['rect'].top += MOVESPEED
        if c['dir'] == DOWNRIGHT:
            c['rect'].left += MOVESPEED
            c['rect'].top += MOVESPEED
        if c['dir'] == UPLEFT:
            c['rect'].left -= MOVESPEED
            c['rect'].top -= MOVESPEED
        if c['dir'] == UPRIGHT:
            c['rect'].left += MOVESPEED
            c['rect'].top -= MOVESPEED

        # Check whether the box has moved out of the window.
        if b['rect'].top < 0:
            # The box has moved past the top.
            if b['dir'] == UPLEFT:
                b['dir'] = DOWNLEFT
            if b['dir'] == UPRIGHT:
                b['dir'] = DOWNRIGHT

        if b['rect'].bottom > WINDOWHEIGHT:
            # The box has moved past the bottom.
            if b['dir'] == DOWNLEFT:
                b['dir'] = UPLEFT
            if b['dir'] == DOWNRIGHT:
                b['dir'] = UPRIGHT
        if b['rect'].left < 0:
            # The box has moved past the left side.
            if b['dir'] == DOWNLEFT:
                b['dir'] = DOWNRIGHT
            if b['dir'] == UPLEFT:
                b['dir'] = UPRIGHT
        if b['rect'].right > WINDOWWIDTH:
            # The box has moved past the right side.
            if b['dir'] == DOWNRIGHT:
                b['dir'] = DOWNLEFT
            if b['dir'] == UPRIGHT:
                b['dir'] = UPLEFT

        # Check whether the circle has moved out of the window.
        if c['rect'].top < 0:
            # The circle has moved past the top.
            if c['dir'] == UPLEFT:
                c['dir'] = DOWNLEFT
            if c['dir'] == UPRIGHT:
                c['dir'] = DOWNRIGHT

        if c['rect'].bottom > WINDOWHEIGHT:
            # The circle has moved past the bottom.
            if c['dir'] == DOWNLEFT:
                c['dir'] = UPLEFT
            if c['dir'] == DOWNRIGHT:
                c['dir'] = UPRIGHT
        if c['rect'].left < 0:
            # The circle has moved past the left side.
            if c['dir'] == DOWNLEFT:
                c['dir'] = DOWNRIGHT
            if c['dir'] == UPLEFT:
                c['dir'] = UPRIGHT
        if c['rect'].right > WINDOWWIDTH:
            # The circle has moved past the right side.
            if c['dir'] == DOWNRIGHT:
                c['dir'] = DOWNLEFT
            if c['dir'] == UPRIGHT:
                c['dir'] = UPLEFT
            

        # Draw the box onto the surface.
        pygame.draw.rect(windowSurface, b['color'], b['rect'])

        # Draw the circles onto the surface.
        pygame.draw.circle(windowSurface, c['color'], c['rect'])

    # Draw the window onto the screen.
    pygame.display.update()
    time.sleep(0.02)
      
