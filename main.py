import pygame
from sys import exit
from random import randint, choice

class Player(pygame.sprite.Sprite): # Player Model
    # sprite class - PyGame OOP part
    # Sprites serve as a convenient container for basic data about an object and and the object as such.
    # That is, you can import images, place them, and define their logic using third-party functions without a class.
    # But changing such objects is a headache.
    # Therefore, sprites are a very good solution not only for the convenience of changing certain objects, but also for code readability
    def __init__(self):
        super().__init__()
        player_walk_1 = pygame.image.load('img/player/run/1.png').convert_alpha() # import player run animation
        player_walk_2 = pygame.image.load('img/player/run/2.png').convert_alpha()
        player_walk_3 = pygame.image.load('img/player/run/3.png').convert_alpha()
        player_walk_4 = pygame.image.load('img/player/run/4.png').convert_alpha()
        player_walk_5 = pygame.image.load('img/player/run/5.png').convert_alpha()
        player_walk_6 = pygame.image.load('img/player/run/6.png').convert_alpha()
        player_walk_7 = pygame.image.load('img/player/run/7.png').convert_alpha()
        player_walk_8 = pygame.image.load('img/player/run/8.png').convert_alpha()
        self.player_walk = [player_walk_1, player_walk_2, player_walk_3, player_walk_4, player_walk_5, player_walk_6, player_walk_7, player_walk_8]
        self.player_walk_index = 0 # later index will be increased to change player run animation

        player_jump_1 = pygame.image.load('img/player/jump/1.png').convert_alpha() # import player jump animation
        player_jump_2 = pygame.image.load('img/player/jump/2.png').convert_alpha()
        player_jump_3 = pygame.image.load('img/player/jump/3.png').convert_alpha()
        self.player_jump = [player_jump_1, player_jump_2, player_jump_3]
        self.player_jump_index = 0 # later index will be increased to change player jump animation

        self.image = self.player_walk[self.player_walk_index] # in sprite class two fields are required: self.image and self.rect to set the sprite image and its position.
        # That is, sprites combine both the position of the image and the image itself.
        self.image = pygame.transform.rotozoom(self.image, 0, 1.5) # scaling player to corrent display
        self.rect = self.image.get_rect(midbottom=(80, 332)) # place player midbotton on x - 80, y - 332
        self.gravity = 0

        self.jump_sound = pygame.mixer.Sound('sounds/jump.mp3') # sound of jump
        self.jump_sound.set_volume(0.1) # fix jump sound volume

    def player_input(self): # check if player jump
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE] and self.rect.bottom >= 332: # if player on the ground, he can jump
            self.gravity = -20
            self.jump_sound.play()

    def apply_gravity(self):
        self.gravity += 1 # to make smooth fall animation
        self.rect.y += self.gravity
        if self.rect.bottom >= 332: # when the bottom of the player model is at y = 332, it will be stopped from falling
            self.rect.bottom = 332
            self.player_jump_index = 0

    def animation(self): # jump and run animation, every frame they will update
        if self.rect.bottom < 332:
            self.player_jump_index += 0.3
            if self.player_jump_index >= len(self.player_jump): self.player_jump_index = len(self.player_jump) - 1
            self.image = self.player_jump[int(self.player_jump_index)]
            self.image = pygame.transform.rotozoom(self.image, 0, 1.5)
        else:
            self.player_walk_index += 0.3
            if self.player_walk_index > len(self.player_walk): self.player_walk_index = 0
            self.image = self.player_walk[int(self.player_walk_index)]
            self.image = pygame.transform.rotozoom(self.image, 0, 1.5)

    def update(self):
        # Another advantage of sprites is that instead of constantly calling different functions
        # to create different conditions and bind them to events,
        # the 'update' function will be responsible for the sprite's behavior.
        self.player_input()
        self.apply_gravity()
        self.animation()

class Enemie(pygame.sprite.Sprite): # Enemies model
    def __init__(self, type):
        super().__init__()

        if type == 'Ground1':
            frame_1 = pygame.image.load('img/enemies/Ground1/1.png').convert_alpha()
            frame_2 = pygame.image.load('img/enemies/Ground1/2.png').convert_alpha()
            frame_3 = pygame.image.load('img/enemies/Ground1/3.png').convert_alpha()
            frame_4 = pygame.image.load('img/enemies/Ground1/4.png').convert_alpha()
            frame_5 = pygame.image.load('img/enemies/Ground1/5.png').convert_alpha()
            frame_6 = pygame.image.load('img/enemies/Ground1/6.png').convert_alpha()
            frame_7 = pygame.image.load('img/enemies/Ground1/7.png').convert_alpha()
            frame_8 = pygame.image.load('img/enemies/Ground1/8.png').convert_alpha()
            frame_9 = pygame.image.load('img/enemies/Ground1/9.png').convert_alpha()
            self.frames = [frame_1, frame_2, frame_3, frame_4, frame_5, frame_6, frame_7, frame_8, frame_9]
            self.frames = [pygame.transform.rotozoom(frame, 0, 0.8) for frame in self.frames]
            y_pos = 336

        if type == 'Ground2':
            frame_1 = pygame.image.load('img/enemies/Ground2/1.png').convert_alpha()
            frame_2 = pygame.image.load('img/enemies/Ground2/2.png').convert_alpha()
            frame_3 = pygame.image.load('img/enemies/Ground2/3.png').convert_alpha()
            frame_4 = pygame.image.load('img/enemies/Ground2/4.png').convert_alpha()
            frame_5 = pygame.image.load('img/enemies/Ground2/5.png').convert_alpha()
            frame_6 = pygame.image.load('img/enemies/Ground2/6.png').convert_alpha()
            frame_7 = pygame.image.load('img/enemies/Ground2/7.png').convert_alpha()
            frame_8 = pygame.image.load('img/enemies/Ground2/8.png').convert_alpha()
            frame_9 = pygame.image.load('img/enemies/Ground2/9.png').convert_alpha()
            self.frames = [frame_1, frame_2, frame_3, frame_4, frame_5, frame_6, frame_7, frame_8, frame_9]
            self.frames = [pygame.transform.rotozoom(frame, 0, 0.8) for frame in self.frames]
            y_pos = 336

        if type == 'Ground3':
            frame_1 = pygame.image.load('img/enemies/Ground3/1.png').convert_alpha()
            frame_2 = pygame.image.load('img/enemies/Ground3/2.png').convert_alpha()
            frame_3 = pygame.image.load('img/enemies/Ground3/3.png').convert_alpha()
            frame_4 = pygame.image.load('img/enemies/Ground3/4.png').convert_alpha()
            frame_5 = pygame.image.load('img/enemies/Ground3/5.png').convert_alpha()
            frame_6 = pygame.image.load('img/enemies/Ground3/6.png').convert_alpha()
            frame_7 = pygame.image.load('img/enemies/Ground3/7.png').convert_alpha()
            frame_8 = pygame.image.load('img/enemies/Ground3/8.png').convert_alpha()
            frame_9 = pygame.image.load('img/enemies/Ground3/9.png').convert_alpha()
            self.frames = [frame_1, frame_2, frame_3, frame_4, frame_5, frame_6, frame_7, frame_8, frame_9]
            self.frames = [pygame.transform.rotozoom(frame, 0, 0.8) for frame in self.frames]
            y_pos = 336

        if type == 'Ground4':
            frame_1 = pygame.image.load('img/enemies/Ground4/1.png').convert_alpha()
            frame_2 = pygame.image.load('img/enemies/Ground4/2.png').convert_alpha()
            frame_3 = pygame.image.load('img/enemies/Ground4/3.png').convert_alpha()
            frame_4 = pygame.image.load('img/enemies/Ground4/4.png').convert_alpha()
            frame_5 = pygame.image.load('img/enemies/Ground4/5.png').convert_alpha()
            frame_6 = pygame.image.load('img/enemies/Ground4/6.png').convert_alpha()
            frame_7 = pygame.image.load('img/enemies/Ground4/7.png').convert_alpha()
            frame_8 = pygame.image.load('img/enemies/Ground4/8.png').convert_alpha()
            self.frames = [frame_1, frame_2, frame_3, frame_4, frame_5, frame_6, frame_7, frame_8]
            self.frames = [pygame.transform.rotozoom(frame, 0, 1.3) for frame in self.frames]
            y_pos = 336

        if type == 'Ground5':
            frame_1 = pygame.image.load('img/enemies/Ground5/1.png').convert_alpha()
            frame_2 = pygame.image.load('img/enemies/Ground5/2.png').convert_alpha()
            frame_3 = pygame.image.load('img/enemies/Ground5/3.png').convert_alpha()
            frame_4 = pygame.image.load('img/enemies/Ground5/4.png').convert_alpha()
            frame_5 = pygame.image.load('img/enemies/Ground5/5.png').convert_alpha()
            frame_6 = pygame.image.load('img/enemies/Ground5/6.png').convert_alpha()
            self.frames = [frame_1, frame_2, frame_3, frame_4, frame_5, frame_6]
            self.frames = [pygame.transform.rotozoom(frame, 0, 1.1) for frame in self.frames]
            y_pos = 340

        if type == 'Ground6':
            frame_1 = pygame.image.load('img/enemies/Ground6/1.png').convert_alpha()
            frame_2 = pygame.image.load('img/enemies/Ground6/2.png').convert_alpha()
            frame_3 = pygame.image.load('img/enemies/Ground6/3.png').convert_alpha()
            frame_4 = pygame.image.load('img/enemies/Ground6/4.png').convert_alpha()
            frame_5 = pygame.image.load('img/enemies/Ground6/5.png').convert_alpha()
            frame_6 = pygame.image.load('img/enemies/Ground6/6.png').convert_alpha()
            frame_7 = pygame.image.load('img/enemies/Ground6/7.png').convert_alpha()
            self.frames = [frame_1, frame_2, frame_3, frame_4, frame_5, frame_6, frame_7]
            self.frames = [pygame.transform.rotozoom(frame, 0, 1.3) for frame in self.frames]
            y_pos = 336

        if type == 'Fly1':
            frame_1 = pygame.image.load('img/enemies/Fly1/1.png').convert_alpha()
            frame_2 = pygame.image.load('img/enemies/Fly1/2.png').convert_alpha()
            frame_3 = pygame.image.load('img/enemies/Fly1/3.png').convert_alpha()
            frame_4 = pygame.image.load('img/enemies/Fly1/4.png').convert_alpha()
            frame_5 = pygame.image.load('img/enemies/Fly1/5.png').convert_alpha()
            frame_6 = pygame.image.load('img/enemies/Fly1/6.png').convert_alpha()
            self.frames = [frame_1, frame_2, frame_3, frame_4, frame_5, frame_6]
            self.frames = [pygame.transform.rotozoom(frame, 0, 1) for frame in self.frames]
            y_pos = 220

        if type == 'Fly2':
            frame_1 = pygame.image.load('img/enemies/Fly2/1.png').convert_alpha()
            frame_2 = pygame.image.load('img/enemies/Fly2/2.png').convert_alpha()
            frame_3 = pygame.image.load('img/enemies/Fly2/3.png').convert_alpha()
            frame_4 = pygame.image.load('img/enemies/Fly2/4.png').convert_alpha()
            frame_5 = pygame.image.load('img/enemies/Fly2/5.png').convert_alpha()
            frame_6 = pygame.image.load('img/enemies/Fly2/6.png').convert_alpha()
            self.frames = [frame_1, frame_2, frame_3, frame_4, frame_5, frame_6]
            self.frames = [pygame.transform.rotozoom(frame, 0, 1) for frame in self.frames]
            y_pos = 220

        self.animation_index = 0
        self.image = self.frames[self.animation_index]
        self.rect = self.image.get_rect(midbottom=(randint(900, 1100), y_pos))

    def animation(self):
        self.animation_index += 0.12
        if self.animation_index > len(self.frames) - 1: self.animation_index = 0
        self.image = self.frames[int(self.animation_index)]

    def update(self):
        self.animation()
        self.rect.x -= 5
        self.destroy()

    def destroy(self): # every time the enemy leaves the user's screen, he will be deleted so as not to take up memory and slow down the game
        if self.rect.x <= -100:
            self.kill()

pygame.init()

screen = pygame.display.set_mode((800, 400)) # creating the main surface - display-surface
pygame.display.set_caption('Not a google dinosaur game...') # icon name
clock = pygame.time.Clock() # create an object to help track time
game_over = True # check if game over
start_time = 0 # for the refresh time after restarting the game, it will change latter
score = 0 # player score

sky = pygame.image.load('img/background/sky.jpg').convert() # import sky image, convert() is used for convenient work with images in the pygame library
sky = pygame.transform.rotozoom(sky, 0, 0.8) # scaling sky to correct display on the screen

ground = pygame.image.load('img/background/ground.png').convert_alpha() # import ground image, convert_aplha() is used for convenient work with images of the 'png' type in the pygame library
ground_rect = ground.get_rect(midbottom=(400, 400)) # In pygame, rectangles help to define the border point at which surface will be placed. That is, in this case, the lower center of the image will be placed at the x - 400 and y - 400 coordinates.

font = pygame.font.Font('font/Pixeltype.ttf', 50) # import custom font to text-labels

music = pygame.mixer.Sound('sounds/music.wav') # import background music
music.set_volume(0.2) # fix bg-music volume
music.play(loops=-1) # with argument 'loops=-1' bg-music will be repeated infinity times

player = pygame.sprite.GroupSingle() # create single sprite group which can contains only 1 sprite object
player.add(Player()) # add player object to single group

enemies = pygame.sprite.Group() # creating sprite group to contain all enemie-sprite class objects

player_menu = pygame.image.load('img/menu/player.png').convert_alpha() # import the player model that will be displayed in the menu
player_menu = pygame.transform.rotozoom(player_menu, 0, 2.4)
player_menu_rectangle = player_menu.get_rect(center=(400, 200))

menu_text = font.render('Not a google dinosaur game...', False, 'White') # text-label with game name
menu_text_rectangle = menu_text.get_rect(center=(400, 80))

menu_screen = pygame.image.load('img/menu/menu.jpg').convert() # import menu image
menu_screen = pygame.transform.rotozoom(menu_screen, 0, 0.9) # scaling the menu image to the corrent display on the screen
menu_screen_rectangle = menu_screen.get_rect(center=(400, 200))

game_start = font.render('Press "SPACE" to start the game', False, 'White') # a text-label that tells the player how to launch the game
game_start_rectangle = game_start.get_rect(center=(400, 320))

event_timer = pygame.USEREVENT + 1 # add 1 more custom event to already exist pygame events
pygame.time.set_timer(event_timer, 1500) # event will be starts every 1.5 seconds

# Function for calculating the score
def game_score():
    current_time = pygame.time.get_ticks() - start_time # The game is counted in seconds, and this line is made so that the counter is reset to zero when you restart after death.
    score_surface = font.render(f"{round(current_time/1000, 0)}"[:-2], False, 'White') # Creating white text-label
    score_rectangle = score_surface.get_rect(center=(400, 40)) # Coordinates when the score will be posted
    screen.blit(score_surface, score_rectangle) # Placing score on the Display-surface
    return f"{round(current_time/1000, 0)}"[:-2] # Return curremt score

# Function for collision between player and enemies
def collision():
    if pygame.sprite.spritecollide(player.sprite, enemies, False): # Check if player touch the enemy, if true
        enemies.empty() # sprite-group with enemie will be cleared
        return True # and game will be over
    else: return False

# A loop to keep the window with the game open
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # To corrent exit the game icon on 'X' in the window corner
            pygame.quit()
            exit()
        if game_over:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE: # Check when game over if pressed 'SPACE' to restart
                game_over = False
                start_time = pygame.time.get_ticks() # To update score

        if not game_over:
            if event.type == event_timer: # Every 1.5s, the enemy will be spawned
                enemies.add(Enemie(choice(['Ground1', 'Ground2', 'Ground3', 'Ground4', 'Ground5', 'Ground6', 'Fly1', 'Fly2']))) # random choice to pick the enemie, what will be spawned

    if not game_over:
        screen.blit(sky, (0, 0)) # background sky-placed on display-surface

        score = game_score() # game score

        player.draw(screen) # draw player-sprite
        player.update() # player place, animation, actions etc.

        enemies.draw(screen) # draw enemies-sprite
        enemies.update() # enemies walk, animation, destruction, etc.

        screen.blit(ground, ground_rect) # placement of the ground-background to make it seem like the player and the opponent are running on the grass

        game_over = collision() # collision function to check if player touch the enemie

    else:
        screen.blit(menu_screen, menu_screen_rectangle) # if the game is over or hasn't started, the player will see a menu
        screen.blit(player_menu, player_menu_rectangle) # player model in the center of window
        screen.blit(menu_text, menu_text_rectangle) # text-label with game name

        if int(score) == 0: # if the game is not running, shows a guide on how to start it
            screen.blit(game_start, game_start_rectangle)
        else: # if a player has already played and lost, they will see their score
            show_score = font.render(f"Your score: {score}", False, 'White')
            show_score_rectangle = show_score.get_rect(center=(400, 320))
            screen.blit(show_score, show_score_rectangle)

    pygame.display.update() # refresh the display to change frames
    clock.tick(60) # 60 frames update per second