import csv

import button
import pygame
import pickle

pygame.init()

clock = pygame.time.Clock()
FPS = 60


# framing game window
screen_width = 1070
screen_height = 800
lower_margin = 35
side_margin = 300

screen = pygame.display.set_mode((screen_width + side_margin, screen_height + lower_margin))
pygame.display.set_caption('Level Editor')

#define game variables
rows = 20
max_cols = 150
tile_size = screen_height // rows
tile_types = 22
level = 0
current_tile = 0



#define game vaariables
scroll_left = False
scroll_right = False
scroll = 0
scroll_speed = 1


#load images:
first_img = pygame.image.load('img7/Background/1.png').convert_alpha()
second_img = pygame.image.load('img7/Background/2.png').convert_alpha()
third_img = pygame.image.load('img7/Background/3.png').convert_alpha()
fourth_img = pygame.image.load('img7/Background/4.png').convert_alpha()
fifth_img = pygame.image.load('img7/Background/5.png').convert_alpha()



#store tiles in a list
img_list = []
for x in range(tile_types):
    img = pygame.image.load(f'img7/tile/{x}.png')
    img = pygame.transform.scale(img, (tile_size, tile_size))
    img_list.append(img)

save_img = pygame.image.load('img7/save_btn.png').convert_alpha()
load_img = pygame.image.load('img7/load_btn.png').convert_alpha()

#define colours
GREEN = (144,201,120)
WHITE = (255,255,255)
RED = (200,25,25)

#define font
font = pygame.font.SysFont('Futura', 30)

#create empty tile list
world_data = []
for row in range(rows):
    r = [-1] * max_cols
    world_data.append(r)

#create ground
for tile in range(0, max_cols):
    world_data[rows - 1][tile] = 0

#function for outputting text onto the screen
def draw_text(text, font, text_col, x,y):
    img = font.render(text, True, text_col)
    screen.blit(img, (x,y))

#create function for drawing background
def draw_bg():
    screen.fill(GREEN)
    width = fifth_img.get_width()
    for x in range(5):
        screen.blit(fifth_img, ((x * width) - scroll * 0.5, 0))
        screen.blit(fourth_img, ((x * width) - scroll * 0.7, screen_height - fourth_img.get_height() - 0))
        screen.blit(third_img, ((x * width) - scroll * 0.8, screen_height - third_img.get_height() - 0))
        screen.blit(second_img, ((x * width) - scroll * 0.9, screen_height - second_img.get_height() - 0))
        screen.blit(first_img, ((x * width) - scroll * 1, 0))
#draw grid
def draw_grid():
    #vertical lines
    for c in range(max_cols + 1):
        pygame.draw.line(screen, WHITE, (c * tile_size-scroll, 0), (c * tile_size - scroll, screen_height))
    #horizontal lines
    for c in range (rows +1):
        pygame.draw.line(screen, WHITE, (0, c * tile_size), (screen_width, c * tile_size))

#funtion for drawing the world tiles
def draw_world():
    for y, row in enumerate(world_data):
        for x, tile in enumerate(row):
            if tile >= 0:
                screen.blit(img_list[tile], (x * tile_size - scroll, y * tile_size))


#create buttons
save_button = button.Button(screen_width // 2, screen_height + lower_margin -50, save_img, 1)
load_button = button.Button(screen_width // 2 + 200, screen_height + lower_margin -50, load_img, 1)
#make a button list
button_list = []
button_col = 0
button_row = 0
for i in range(len(img_list)):
    tile_button = button.Button(screen_width + (75 * button_col) + 50, 75 * button_row + 50, img_list[i], 1)
    button_list.append(tile_button)
    button_col += 1
    if button_col == 3:
        button_row += 1
        button_col = 0


run = True
while run:

    clock.tick(FPS)

    draw_bg()
    draw_grid()
    draw_world()


    draw_text(f'Level: {level}', font,RED,10, screen_height + lower_margin -30)
    draw_text('Press UP or DOWN to change level', font, RED, 100, screen_height + lower_margin - 30)

    #save and load data
    if save_button.draw(screen):
        # save level data
        with open(f'level{level}_data.csv', 'w', newline='') as csvfile:
            writer = csv.writer(csvfile, delimiter=',')
            for row in world_data:
                writer.writerow(row)
    # alternative pickle method
    # pickle_out = open(f'level{level}_data', 'wb')
    # pickle.dump(world_data, pickle_out)
    # pickle_out.close()
    if load_button.draw(screen):
        # load in level data
        # reset scroll back to the start of the level
        scroll = 0
        with open(f'level{level}_data.csv', newline='') as csvfile:
            reader = csv.reader(csvfile, delimiter=',')
            for x, row in enumerate(reader):
                for y, tile in enumerate(row):
                    world_data[x][y] = int(tile)

    #draw tile panel and tiles
    pygame.draw.rect(screen, GREEN, (screen_width, 0, side_margin, screen_height))

    #choose a tile
    button_count = 0
    for button_count, i in enumerate(button_list):
        if i.draw(screen):
            current_tile = button_count

    #highlisght the selected title
    pygame.draw.rect(screen, RED, button_list[current_tile].rect, 3)

    #scroll the map
    if scroll_left == True and scroll > 0:
        scroll -= 5 + scroll_speed
    if scroll_right == True and scroll < (max_cols * tile_size) - screen_width:
        scroll += 5 + scroll_speed

    pos = pygame.mouse.get_pos()
    x = (pos[0] + scroll) // tile_size
    y = pos[1] // tile_size

    #check that the coordinates are within the tiles areas
    if pos[0] < screen_width and pos[1] < screen_height:
        #update tile value
        if pygame.mouse.get_pressed()[0] == 1:
            if world_data[y][x] != current_tile:
                world_data[y][x] = current_tile
        if pygame.mouse.get_pressed()[2] == 1:
            world_data[y][x] = -1

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        #keyboard presses
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                level += 1
            if event.key == pygame.K_DOWN:
                level -= 1
            if event.key == pygame.K_LEFT:
                scroll_left = True
            if event.key == pygame.K_RIGHT:
                scroll_right = True
            if event.key == pygame.K_RSHIFT:
                scroll_speed = 5
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                scroll_left = False
            if event.key == pygame.K_RIGHT:
                scroll_right = False
            if event.key == pygame.K_RSHIFT:
                scroll_speed = 1

    pygame.display.update()

pygame.quit()