import sys
try:
    import pygame
except ModuleNotFoundError:
    print("use: pip install pygame")
    sys.exit()



import random
#if error.
#run "pip install pygame" in console.
game_board_height = 1000
game_board_width = 1900
score = 0
scoreMult = 1

death_block_color = (199, 4, 23)
vertical_bocks_speed = 10
horisontal_bocks_speed = 15

vertical_block_height = 0.5 *game_board_height
vertical_block_width = 0.1* game_board_width

horisontal_block_height = 0.2* game_board_height
horisontal_block_width =0.7 * game_board_width


sheild_radius_item = 50
sheild_radius_held = 30

sheild_color_item = (5, 103, 250)
sheild_color_held = (5, 209, 250)


current_blocks = []
# x and y are decided in the moment

# Initialize Pygame
pygame.init()

# Set up screen
screen = pygame.display.set_mode((game_board_width, game_board_height))
pygame.display.set_caption("powercreeps")

# Create a font object
font = pygame.font.SysFont(None, 40)  # None = default font, 36 = font size

# Set initial mouse position to center
cursor_x, cursor_y = game_board_width/2 ,game_board_height/2
pygame.mouse.set_pos(cursor_x, cursor_y)

# Clock for controlling frame rate
clock = pygame.time.Clock()

# Movement speed
speed = 15
lost = False
mdisplay = False
loop =0
# Main game loop
while not lost:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        #if use of "q"-key, script terminates.    
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                pygame.quit()
                sys.exit()

    # Get key states
    keys = pygame.key.get_pressed()

    # Update cursor position based on arrow keys
    if keys[pygame.K_LEFT] or keys[pygame.K_a]:
        cursor_x -= speed
    if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
        cursor_x += speed
    if keys[pygame.K_UP] or keys[pygame.K_w]:
        cursor_y -= speed
    if keys[pygame.K_DOWN] or keys[pygame.K_s]:
        cursor_y += speed
    #if use of "Esc"-key, script terminates.    
    if keys[pygame.K_ESCAPE]:
        pygame.quit()
        sys.exit()
    if keys[pygame.K_0] and (keys[pygame.K_LCTRL] or keys[pygame.K_RCTRL]):
        lost = True
    if keys[pygame.K_m] and (keys[pygame.K_LCTRL] or keys[pygame.K_RCTRL]):
        mdisplay = True
    # Keep cursor within the screen bounds
    cursor_x = max(0, min(cursor_x, game_board_width-1))
    cursor_y = max(0, min(cursor_y, game_board_height-1))

    # Set the new cursor position
    pygame.mouse.set_pos((cursor_x, cursor_y))
    
    mouse_x, mouse_y = pygame.mouse.get_pos()
    cursor_col = pygame.Rect(mouse_x, mouse_y, 10, 10)

    #info print to terminal 
    # print(f"Cursor position: x={mouse_x}, y={mouse_y}")
   
  
    
    # Render text info for use on screen
    text_info = font.render(f"Bruk Q eller Esc for avslutt.", True, (255, 255, 255))  # White color
    text_surface = font.render(f"score: {round(score* scoreMult,1)}",True,(255,255,255)) 
    mouse_pos = font.render(f"mouse x: {mouse_x} mouse y: {mouse_y}",True,(255,255,255))
    # Optional: Clear screen and update.
    screen.fill((30, 30, 30))
    
    screen.blit(text_info, (10, 10))
  
    screen.blit(text_surface, (10, 40))
    if mdisplay:
        screen.blit(mouse_pos,(10,70))

    match score- loop:
        case 30:
            block1 = [[random.randint(0,game_board_width-1),-vertical_block_height, vertical_block_width,vertical_block_height], "down"]
            current_blocks.append(block1)
          
        case 110:
            block2 = [[game_board_width,random.randint(0,game_board_height-1), horisontal_block_width,horisontal_block_height], "left"]
            current_blocks.append(block2)
        case 80:
            block3 = [[-horisontal_block_width,random.randint(0,game_board_height-1), horisontal_block_width,horisontal_block_height], "right"]
            current_blocks.append(block3)
        case 140:
            block1 = [[random.randint(0,game_board_width-1),game_board_height, vertical_block_width,vertical_block_height], "up"]
            current_blocks.append(block1)
        case 150:
            loop +=150
            scoreMult += 0.2
    now_blocks = current_blocks
    for item in now_blocks:
        if item[1]== "down":
            #   print("it work")
            item[0][1] = item[0][1] +vertical_bocks_speed + loop/150*2
            if item[0][1] == game_board_height:
                current_blocks.remove(item)
        elif item[1] == "up":
                 #   print("it work")
            item[0][1] = item[0][1] -vertical_bocks_speed - loop/150*2
            if item[0][1] == -vertical_block_height:
                current_blocks.remove(item)

        elif item[1] == "left":
                #   print("it work")
            item[0][0] = item[0][0] -horisontal_bocks_speed  - loop/150*2
            if item[0][0] == game_board_width:
                current_blocks.remove(item)
        elif item[1] == "right":
            #   print("it work"d)
            item[0][0] = item[0][0] +horisontal_bocks_speed  + loop/150*2
            if item[0][0] == -horisontal_block_width:
                current_blocks.remove(item)


        

        pygame.draw.rect(screen,death_block_color,item[0])
        block_rect = pygame.Rect(item[0])
        if cursor_col.colliderect(block_rect):
            lost = True
          
    pygame.display.flip()
    score += 1 


    # Cap the frame rate
    clock.tick(60)
print(f"your score is: {round(score*scoreMult,1)}")