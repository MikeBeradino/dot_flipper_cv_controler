import pygame
import random
import math

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

WIDTH = 26
HEIGHT = 26
MARGIN = 5
window_w = 770
window_h = 770

# set the array
grid = []
for row in range(28):
    grid.append([])
    for column in range(28):
        grid[row].append(0)

pygame.init()
# Set the width and height of the screen [width, height]
size = [window_w, window_h]
screen = pygame.display.set_mode(size)
# Loop until the user clicks the close button.
done = False
# Used to manage how fast the screen updates
clock = pygame.time.Clock()

block_size = 1
velocity = [31, 31]

pos_x = 62
pos_y = 403

drawstar = False
draw_circle = False
star_counter = 0
circle_counter = 0

# -------- Main Program Loop -----------
# while not done:
# --- Main event loop
while not done:
    oldpos_x = pos_x
    oldpos_y = pos_y

    pos_x += velocity[0]
    pos_y += velocity[1]

    column = round(pos_x // (WIDTH + MARGIN))
    row = round(pos_y // (HEIGHT + MARGIN))

    column_old =  round(oldpos_x // (WIDTH + MARGIN))
    row_old = round(oldpos_y // (HEIGHT + MARGIN))

    #bouncing block
    print (grid[int(row)][int(column)])
    if pos_x + block_size > window_w or pos_x < 0 or  grid[int(row)][int(column)] == 1 :
        velocity[0] = -velocity[0]
       # velocity[0] = -velocity[0] - 1 * random.uniform(0, 1)


    if pos_y + block_size > window_h or pos_y < 0 or  grid[int(row)][int(column)] == 1 :
        velocity[1] = -velocity[1]


    grid[int(row_old)][int(column_old)] = 0
    grid[int(row)][int(column)] = 1

    '''
    if star_counter <= 3 and drawstar == True:

        pos = pygame.mouse.get_pos()
        column = pos[0] // (WIDTH + MARGIN)
        row = pos[1] // (HEIGHT + MARGIN)

        grid[row - star_counter][column ] = 1
        grid[row + star_counter][column ] = 1
    '''
    # draw the circle
    if circle_counter <=6 and draw_circle == True:
        pos = pygame.mouse.get_pos()
        column = pos[0] // (WIDTH + MARGIN)
        row = pos[1] // (HEIGHT + MARGIN)
        r = circle_counter
        print(r)
        for angle in range(0, 360, 5):
            x = r * math.sin(math.radians(angle)) + (column)
            y = r * math.cos(math.radians(angle)) + (row)
            # keeps everything in bounds
            if y+1 >= len(grid):
                y = len(grid)-1
            if x+1 >= len(grid):
                x = len(grid)-1
            if y < 0:
                y = 0
            if x < 0:
                x=0
            grid[int(round(y))][int(round(x))] = 1

            x = (r-1) * math.sin(math.radians(angle)) + (column)
            y = (r-1) * math.cos(math.radians(angle)) + (row)
            # keeps everything in bounds
            if y + 1 >= len(grid):
                y = len(grid) - 1
            if x + 1 >= len(grid):
                x = len(grid) - 1
            if y < 0:
                y = 0
            if x < 0:
                x = 0
            # print(x,y)
            grid[int(round(y))][int(round(x))] = 0


        circle_counter = circle_counter +1
       # if star_counter == 3:
        #    draw_circle = False
        #grid[row - star_counter][column - star_counter] = 1
        #grid[row - star_counter][column - star_counter] = 1
        #grid[row + star_counter][column - star_counter] = 1
        #star_counter = star_counter + 1
       # if star_counter == 3:
        #    drawstar = False

    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            done = True  # Flag that we are done so we exit this loop

        if event.type == pygame.MOUSEBUTTONDOWN:
            # User clicks the mouse. Get the position
            pos = pygame.mouse.get_pos()
            # Change the x/y screen coordinates to grid coordinates
            column = pos[0] // (WIDTH + MARGIN)
            row = pos[1] // (HEIGHT + MARGIN)
            # Set that location to one
            grid[row][column] = 1
           # print("here2")
            star_counter = 0
            circle_counter = 0
            draw_circle = True
            print("Click ", pos, "Grid coordinates: ", row, column)

        elif event.type != pygame.mouse.get_pos():
            pos = pygame.mouse.get_pos()
            column = pos[0] // (WIDTH + MARGIN)
            row = pos[1] // (HEIGHT + MARGIN)
            print("Click ", pos, "Grid coordinates: ", row, column)

    screen.fill(BLACK)
    # --- Drawing code should go here
    # Draw the grid
    for row in range(25):
        for column in range(25):
            color = WHITE
            if grid[row][column] == 1:
                color = BLACK
            pygame.draw.rect(screen, color, [(MARGIN + WIDTH) * column + MARGIN,(MARGIN + HEIGHT) * row + MARGIN, WIDTH, HEIGHT])
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
    # --- Limit to 60 frames per second
    clock.tick(10)
# Close the window and quit.
pygame.quit()